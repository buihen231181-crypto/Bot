import os
import threading
from flask import Flask
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# ==========================================
# 1. KHỞI TẠO WEB SERVER (Giữ Render sống 24/7)
# ==========================================
app = Flask(__name__)

@app.route('/')
def home():
    return "Bot Telegram đang hoạt động 24/7!"

def run_web():
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)

# Chạy Flask ở luồng riêng ngầm
threading.Thread(target=run_web, daemon=True).start()


# ==========================================
# 2. XỬ LÝ LỆNH CỦA BOT TELEGRAM
# ==========================================
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Chảo bạn! Bot Crypto đã hoạt động thành công trên Render!")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Các lệnh hiện có:\n/start - Kiểm tra hoạt động\n/help - Hướng dẫn")


# ==========================================
# 3. CHẠY BOT
# ==========================================
def main():
    token = os.environ.get("BOT_TOKEN")
    if not token:
        print("LỖI: Chưa cài đặt biến BOT_TOKEN trên Render!")
        return

    application = ApplicationBuilder().token(token).build()

    application.add_handler(CommandHandler("start", start_command))
    application.add_handler(CommandHandler("help", help_command))

    print("Bot Telegram bắt đầu lắng nghe tin nhắn...")
    application.run_polling()

if __name__ == '__main__':
    main()
