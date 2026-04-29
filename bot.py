import asyncio
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = "8635388398:AAHpqA1GyCMEiUXerWCxLZoyKTtfk8Jxric"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Send numbers to check")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Processing...")
    
    await asyncio.sleep(2)

    numbers = update.message.text.split("\n")
    result = []

    for num in numbers:
        if len(num) >= 10:
            result.append(f"{num} 🟢 Fresh Num")
        else:
            result.append(f"{num} 🔴 Invalid")

    await update.message.reply_text("\n".join(result))

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT, handle_message))

app.run_polling()