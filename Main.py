import discord
from discord.ext import commands
import os

intents = discord.Intents.default()
intents.message_content = True
intents.members = True
intents.reactions = True

bot = commands.Bot(command_prefix="!", intents=intents, help_command=None)

@bot.event
async def on_ready():
    print(f'Life-bot online! {bot.user}')

# --- QUANDO MARCAM O BOT ---
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if bot.user.mentioned_in(message):
        await message.reply("SÓ SALVINHO")

    await bot.process_commands(message)

# --- QUANDO REAGEM COM ✅ OU ❌ ---
@bot.event
async def on_raw_reaction_add(payload):
    if payload.user_id == bot.user.id:
        return

    canal = bot.get_channel(payload.channel_id)
    guild = bot.get_guild(payload.guild_id)
    member = guild.get_member(payload.user_id)

    if str(payload.emoji) == "✅":
        await canal.send(f"{member.mention} parabéns sua tag tá liberada🎉")

    elif str(payload.emoji) == "❌":
        await canal.send(f"{member.mention} ops entre na comunidade pra receber a tag!")

# --- COMANDOS ---
@bot.command()
async def ping(ctx):
    await ctx.send('Life-bot online! 🏆')

@bot.command()
async def help(ctx):
    embed = discord.Embed(title="Comandos Gold Life", color=0xFFD700)
    embed.add_field(name="!clear [numero]", value="Apaga mensagens", inline=False)
    embed.add_field(name="!kick @pessoa", value="Expulsa", inline=False)
    embed.add_field(name="!ban @pessoa", value="Bane", inline=False)
    embed.add_field(name="Reação ✅", value="Libera tag", inline=False)
    embed.add_field(name="Reação ❌", value="Pede pra entrar na comunidade", inline=False)
    await ctx.send(embed=embed)

@bot.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount: int = 5):
    await ctx.channel.purge(limit=amount + 1)
    await ctx.send(f'✅ {amount} apagadas!', delete_after=3)

@bot.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason="Sem motivo"):
    await member.kick(reason=reason)
    await ctx.send(f'👢 {member.mention} expulso!')

@bot.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason="Sem motivo"):
    await member.ban(reason=reason)
    await ctx.send(f'🔨 {member.mention} BANIDO!')

bot.run(os.getenv("DISCORD_TOKEN"))
