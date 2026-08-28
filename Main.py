import os
from flask import Flask
import threading
import discord
from discord.ext import commands

app = Flask(__name__)
@app.route('/')
def home():
    return "Life Bot ONLINE"

def run_flask():
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)

threading.Thread(target=run_flask).start()

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents, help_command=None)

@bot.event
async def on_ready():
    print(f"ONLINE - Logado como {bot.user}")

@bot.event
async def on_message(message):
    if message.author.bot: return
    if bot.user.mentioned_in(message):
        await message.channel.send("SÓ SALVINHO 😎💛")
    await bot.process_commands(message)

@bot.command()
async def ping(ctx):
    await ctx.send("Life 24h ON! 🏆")

@bot.command()
async def travar(ctx):
    await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=False)
    await ctx.send("🔒 Travado!")

@bot.command()
async def destravar(ctx):
    await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=True)
    await ctx.send("🔓 Destravado!")

@bot.command()
async def limpar(ctx, qtd: int = 10):
    await ctx.channel.purge(limit=qtd+1)

@bot.command()
async def anuncio(ctx, *, texto):
    embed = discord.Embed(title="📢 AVISO GOLD LIFE", description=texto, color=0xFFD700)
    await ctx.send("@everyone", embed=embed)

bot.run(os.getenv("DISCORD_TOKEN"))
