import time
import psutil
import requests

BOT_TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"
CHAT_ID = "YOUR_CHAT_ID"
CPU_THRESHOLD = 85.0
RAM_THRESHOLD = 85.0
CHECK_INTERVAL = 60  # seconds

def send_alert(message: str):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": message}
    try:
        requests.post(url, json=payload, timeout=10)
    except requests.RequestException as e:
        print(f"Failed to send alert: {e}")

def monitor_system():
    print("Starting sys-alert-bot...")
    while True:
        cpu = psutil.cpu_percent(interval=1)
        ram = psutil.virtual_memory().percent
        if cpu > CPU_THRESHOLD or ram > RAM_THRESHOLD:
            msg = f"⚠️ System Alert!\nCPU Usage: {cpu}%\nRAM Usage: {ram}%"
            send_alert(msg)
        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    monitor_system()
