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
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"ONLINE - Logado como {bot.user}")
    await bot.tree.sync()

TOKEN = os.getenv("DISCORD_TOKEN")
bot.run(TOKEN)
