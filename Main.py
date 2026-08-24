import os
from flask import Flask
from threading import Thread
from telegram import Update
from telegram.ext import Application, ContextTypes, MessageReactionHandler, MessageHandler, filters

TOKEN = os.getenv("BOT_TOKEN")
web_app = Flask(__name__)

@web_app.route('/')
def home():
    return "Life-bot online!"

async def reacoes(update: Update, context: ContextTypes.DEFAULT_TYPE):
    r = update.message_reaction
    if not r: return
    emojis = [x.emoji for x in r.new_reaction]
    if "✅" in emojis:
        await context.bot.send_message(chat_id=r.chat_id, text="Salvo! ✅")
    if "❌" in emojis:
        await context.bot.send_message(chat_id=r.chat_id, text="Removido! ❌")

async def marcar(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("SÓ SALVINHO 😎")

def run_bot():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(MessageReactionHandler(reacoes))
    app.add_handler(MessageHandler(filters.Mention("@MeuLife_Bot"), marcar))
    app.add_handler(MessageHandler(filters.REPLY, marcar))
    print("BOT ON")
    app.run_polling()

if __name__ == "__main__":
    Thread(target=run_bot).start()
    port = int(os.environ.get("PORT", 10000))
    web_app.run(host='0.0.0.0', port=port)
