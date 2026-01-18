import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
from database import get_test_data

BOT_TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    data = get_test_data()
    message = f"Тестовые данные: {data}"
    await update.message.reply_text(message)

if __name__ == "__main__":
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()