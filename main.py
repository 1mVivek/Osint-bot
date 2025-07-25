import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    ContextTypes,
)
from osint_tools import ip_lookup, email_breach_check, phone_lookup

# Load environment variables
load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")

if not TOKEN:
    raise ValueError("❌ BOT_TOKEN is missing in .env file!")

# Build Telegram bot app
app = ApplicationBuilder().token(TOKEN).build()

# /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Welcome to OSINT Bot!\n\n"
        "Available commands:\n"
        "/ipinfo <ip or domain>\n"
        "/emailcheck <email>\n"
        "/phonecheck <number>"
    )

# /ipinfo command
async def ipinfo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("⚠️ Please provide an IP or domain.")
        return
    ip = context.args[0]
    result = ip_lookup(ip)
    await update.message.reply_text(result)

# /emailcheck command
async def emailcheck(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("⚠️ Please provide an email.")
        return
    email = context.args[0]
    result = email_breach_check(email)
    await update.message.reply_text(result)

# /phonecheck command
async def phonecheck(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("⚠️ Please provide a phone number.")
        return
    number = context.args[0]
    result = phone_lookup(number)
    await update.message.reply_text(result)

# Register handlers
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("ipinfo", ipinfo))
app.add_handler(CommandHandler("emailcheck", emailcheck))
app.add_handler(CommandHandler("phonecheck", phonecheck))

# Start the bot
if __name__ == "__main__":
    print("🤖 OSINT Bot is running...")
    app.run_polling()
