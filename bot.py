from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackContext
import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
TARGET_GROUP_ID = os.getenv("TARGET_GROUP_ID")

async def ask_command(update: Update, context: CallbackContext) -> None:
    """Handles the /ask command and forwards the message to the group."""
    if not context.args:
        await update.message.reply_text("Usage: /ask your question here.")
        return

    message_text = " ".join(context.args)

    await context.bot.send_message(chat_id=TARGET_GROUP_ID, text=f"📢 *New Message:*\n{message_text}", parse_mode="Markdown")
    
    await update.message.reply_text("✅ Your message has been forwarded!")

def main():
    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("ask", ask_command))

    app.run_polling()

if __name__ == "__main__":
    print("Bot started!")
    main()
