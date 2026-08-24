import os
from telegram import Update
from telegram.ext import Application, ContextTypes, MessageReactionHandler, MessageHandler, filters

TOKEN = os.getenv("BOT_TOKEN")

async def reacoes(update: Update, context: ContextTypes.DEFAULT_TYPE):
    r = update.message_reaction
    if not r: return
    emojis = [x.emoji for x in r.new_reaction if hasattr(x, 'emoji')]
    if "✅" in emojis:
        await context.bot.send_message(chat_id=r.chat.id, reply_to_message_id=r.message_id, text="✅ **Parabéns!**\n\nVocê está com a tag na **GOLD LIFE** 🔥\n\n> SÓ SALVINHO", parse_mode="Markdown")
    if "❌" in emojis:
        await context.bot.send_message(chat_id=r.chat.id, reply_to_message_id=r.message_id, text="❌ **Acesso negado**\n\nEntre na comunidade pra receber a tag.\n\n> SÓ SALVINHO", parse_mode="Markdown")

async def marcar(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("SÓ SALVINHO 😎")

app = Application.builder().token(TOKEN).build()
app.add_handler(MessageReactionHandler(reacoes))
app.add_handler(MessageHandler(filters.Mention("@MeuLife_Bot") | filters.Regex("@MeuLife_Bot"), marcar))
app.add_handler(MessageHandler(filters.REPLY, marcar))
print("BOT ON")
app.run_polling()
