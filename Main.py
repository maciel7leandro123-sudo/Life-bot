import discord
from discord.ext import commands
import os
from flask import Flask
import threading

app = Flask(__name__)

@app.route('/')
def home():
    return "Bot online!"

def run_flask():
    app.run(host='0.0.0.0', port=10000)

threading.Thread(target=run_flask).start()

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Logado como {bot.user}")

@bot.command()
async def ping(ctx):
    await ctx.send("Life-bot online! 🏆🔥")

bot.run(os.getenv("DISCORD_TOKEN"))
