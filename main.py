
import threading
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is running!"

def run_web():
    app.run(host='0.0.0.0', port=10000)

# Chạy Web Server ở luồng ngầm để Render không bị tắt
threading.Thread(target=run_web, daemon=True).start()

# --- CODE BOT TELEGRAM CỦA BẠN Ở DƯỚI NÀY ---
