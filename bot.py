from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import os

BOT_TOKEN = os.getenv("BOT_TOKEN", "8171626569:AAHFCwYirjMnGsa-UQApf_2fmVvid1aISU0")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    result = 1 + 1
    await update.message.reply_text(f"1 + 1 = {result}")

if __name__ == "__main__":
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()