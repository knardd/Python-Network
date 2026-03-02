import os
import requests
from dotenv import load_dotenv

# 1. Load data dari file .env
load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

def kirim_test():
    pesan = "🚀 Test Koneksi: Bot Telegram sudah berhasil terhubung dengan Python!"
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    
    payload = {
        "chat_id": CHAT_ID,
        "text": pesan,
        "parse_mode": "HTML" # Agar bisa pakai format tebal/miring
    }

    try:
        respon = requests.post(url, data=payload)
        if respon.status_code == 200:
            print("✅ Berhasil! Cek HP Anda, pesan sudah masuk.")
        else:
            print(f"❌ Gagal. Error: {respon.text}")
    except Exception as e:
        print(f"⚠️ Terjadi error koneksi: {e}")

if __name__ == "__main__":
    kirim_test()