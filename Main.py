import discord
from discord.ext import commands
import os
from flask import Flask
import threading

# Mantém a porta aberta pro Render não dar erro
app = Flask(__name__)
@app.route('/')
def home():
    return "Life Bot ONLINE!"

def run_flask():
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)

threading.Thread(target=run_flask).start()

# SEU BOT
intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)

OWNER_ID = 1297981646842237049

@bot.event
async def on_ready():
    print(f"ONLINE Gold Life - Logado como {bot.user}")
    try:
        synced = await bot.tree.sync()
        print(f"{len(synced)} comandos sincronizados")
    except Exception as e:
        print(e)

# COLE SEUS COMANDOS AQUI EMBAIXO (os que eu já te mandei)

TOKEN = os.getenv("DISCORD_TOKEN")
if not TOKEN:
    print("ERRO: Coloca o DISCORD_TOKEN no Environment do Render!")
else:
    bot.run(TOKEN)
