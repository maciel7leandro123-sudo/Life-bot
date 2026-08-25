import discord
from discord.ext import commands
import datetime

intents = discord.Intents.default()
intents.message_content = True
intents.members = True
intents.reactions = True

bot = commands.Bot(command_prefix="!", intents=intents, help_command=None)

@bot.event
async def on_ready():
    print(f"Life-bot online! {bot.user}")

@bot.event
async def on_message(message):
    if bot.user.mentioned_in(message) and not message.mention_everyone:
        if len(message.mentions) == 1:
            await message.channel.send("SÓ SALVINHO")
    await bot.process_commands(message)

@bot.event
async def on_raw_reaction_add(payload):
    if payload.user_id == bot.user.id:
        return
    
    channel = bot.get_channel(payload.channel_id)
    try:
        msg = await channel.fetch_message(payload.message_id)
        autor_da_mensagem = msg.author  # PESSOA QUE RECEBEU A REAÇÃO

        if str(payload.emoji) == "✅":
            await channel.send(f"{autor_da_mensagem.mention} parabéns sua tag tá liberada🎉")
        elif str(payload.emoji) == "❌":
            await channel.send(f"{autor_da_mensagem.mention} ops entre na comunidade pra receber a tag!")

    except:
        pass

@bot.command()
async def ping(ctx):
    await ctx.send("Life-bot online! 🏆")

@bot.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, qtd: int = 5):
    await ctx.channel.purge(limit=qtd+1)
    await ctx.send(f"Apaguei {qtd} mensagens!", delete_after=3)

@bot.command()
@commands.has_permissions(moderate_members=True)
async def castigo(ctx, membro: discord.Member, tempo: str, *, motivo="Sem motivo"):
    # tempo tipo: 10m, 1h, 1d
    try:
        unidade = tempo[-1]
        valor = int(tempo[:-1])
        
        if unidade == "m":
            delta = datetime.timedelta(minutes=valor)
        elif unidade == "h":
            delta = datetime.timedelta(hours=valor)
        elif unidade == "d":
            delta = datetime.timedelta(days=valor)
        else:
            await ctx.send("Use m para minutos, h para horas, d para dias. Ex: !castigo @fulano 10m spam")
            return

        await membro.timeout(delta, reason=motivo)
        await ctx.send(f"🔨 {membro.mention} levou castigo de {tempo}! Motivo: {motivo}")

    except Exception as e:
        await ctx.send(f"Erro: {e}. Use assim: !castigo @pessoa 10m motivo")

@bot.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, membro: discord.Member, *, motivo="Sem motivo"):
    await membro.kick(reason=motivo)
    await ctx.send(f"{membro.mention} foi expulso!")

@bot.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, membro: discord.Member, *, motivo="Sem motivo"):
    await membro.ban(reason=motivo)
    await ctx.send(f"{membro.mention} foi banido!")

import os
TOKEN = os.getenv("DISCORD_TOKEN")
bot.run(TOKEN)

