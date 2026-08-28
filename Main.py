import discord
from discord.ext import commands
import datetime
import os

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents, help_command=None)

DONO_ID = 1297981646842237049

@bot.event
async def on_ready():
    print(f"✅ LIFE FINAL ONLINE: {bot.user}")
    await bot.change_presence(activity=discord.Game(name="GOLD LIFE 24H ON 💛"))

@bot.event
async def on_message(message):
    if message.author.bot:
        return
    if bot.user.mentioned_in(message) and not message.mention_everyone:
        if len(message.mentions) == 1:
            await message.channel.send("SÓ SALVINHO 💛 24H ON")
    await bot.process_commands(message)

def eh_dono():
    async def predicate(ctx):
        return ctx.author.id == DONO_ID or ctx.guild.owner_id == ctx.author.id or ctx.author.guild_permissions.administrator
    return commands.check(predicate)

@bot.command()
@eh_dono()
async def ban(ctx, membro: discord.Member, *, motivo="Sem motivo"):
    await membro.ban(reason=motivo)
    await ctx.send(f"🔨 {membro.mention} foi BANIDO! Motivo: {motivo}")

@bot.command()
@eh_dono()
async def kick(ctx, membro: discord.Member, *, motivo="Sem motivo"):
    await membro.kick(reason=motivo)
    await ctx.send(f"👢 {membro.mention} foi EXPULSO! Motivo: {motivo}")

@bot.command()
@eh_dono()
async def castigo(ctx, membro: discord.Member, tempo: str, *, motivo="Sem motivo"):
    try:
        unidade = tempo[-1].lower()
        valor = int(tempo[:-1])
        if unidade == "m": delta = datetime.timedelta(minutes=valor)
        elif unidade == "h": delta = datetime.timedelta(hours=valor)
        elif unidade == "d": delta = datetime.timedelta(days=valor)
        else: 
            await ctx.send("Use: !castigo @pessoa 10m / 1h / 1d")
            return
        await membro.timeout(delta, reason=motivo)
        await ctx.send(f"⏰ {membro.mention} de castigo por {tempo}! Motivo: {motivo}")
    except Exception as e:
        await ctx.send(f"Erro: {e}")

@bot.command()
@eh_dono()
async def limpar(ctx, qtd: int = 10):
    await ctx.channel.purge(limit=qtd+1)
    await ctx.send(f"🧹 Limpei {qtd} mensagens!", delete_after=3)

@bot.command()
@eh_dono()
async def travar(ctx):
    await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=False)
    await ctx.send("🔒 Chat travado!")

@bot.command()
@eh_dono()
async def destravar(ctx):
    await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=True)
    await ctx.send("🔓 Chat destravado!")

@bot.command()
@eh_dono()
async def anuncio(ctx, *, texto):
    embed = discord.Embed(title="📢 GOLD LIFE", description=texto, color=0xFFD700)
    await ctx.send("@everyone", embed=embed)

@bot.command()
async def ping(ctx):
    await ctx.send("💛 LIFE 24H ON! Dono: <@1297981646842237049>")

bot.run(os.getenv("DISCORD_TOKEN"))
