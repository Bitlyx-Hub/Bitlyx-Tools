import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

load_dotenv()
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "Welcome! Use /add [text] to submit a request."
    )


async def add(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if not context.args:
        await update.message.reply_text("Usage: /add [text]")
        return

    user_id = update.effective_user.id
    message_text = " ".join(context.args)

    with open("requests.txt", "a") as f:
        f.write(f"User ID: {user_id} | Message: {message_text}\n")

    await update.message.reply_text("Request saved!")


def main() -> None:
    application = Application.builder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("add", add))

    application.run_polling()


if __name__ == "__main__":
    main()
