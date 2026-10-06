import os
import asyncio
import json
from datetime import datetime, timezone, timedelta
from telethon import TelegramClient, events
from dotenv import load_dotenv

load_dotenv()

# Load config
with open('config.json', 'r') as file:
    config = json.load(file)

TARGET_BOT = config.get('target_bot')
LAYANAN = config.get('layanan').lower()
JUMLAH_PESANAN_STR = f"{config.get('jumlah_pesanan')}x"

_original_print = print
def print(*args, **kwargs):
    tz_gmt7 = timezone(timedelta(hours=7))
    now = datetime.now(tz_gmt7).strftime('%H:%M:%S')
    _original_print(f"[{now}]", *args, **kwargs)

# Ganti dengan API ID dan API Hash di env
API_ID = int(os.getenv('API_ID'))
API_HASH = os.getenv('API_HASH')

SESSION_NAME = 'notif'

client = TelegramClient(SESSION_NAME, API_ID, API_HASH)

@client.on(events.NewMessage(chats=TARGET_BOT, pattern='(?i).*nomor baru.*'))
async def on_nomor_baru(event):
    print("Mendeteksi pesan yang mengandung 'Nomor baru'. Membalas dengan '/layanan'...")
    await event.reply('/layanan')

@client.on(events.NewMessage(chats=TARGET_BOT))
async def on_layanan_reply(event):
    if event.message.buttons:
        for row in event.message.buttons:
            for button in row:
                if LAYANAN in button.text.lower():
                    print(f"Menemukan tombol '{button.text}', mengkliknya...")
                    await button.click()
                    return 

@client.on(events.MessageEdited(chats=TARGET_BOT))
async def on_message_edited(event):
    if event.raw_text and 'sedang kosong' in event.raw_text.lower():
        print("Pesan terupdate menyatakan 'sedang kosong'. Mengabaikan dan menunggu pesan 'Nomor baru' selanjutnya...")
        return
    if event.message.buttons:
        button_2x = None
        button_konfirmasi = None
        is_2x_clicked = False
        
        for row in event.message.buttons:
            for button in row:
                text_lower = button.text.lower()
                if JUMLAH_PESANAN_STR in text_lower:
                    button_2x = button
                    if '✅' in text_lower:
                        is_2x_clicked = True
                elif 'konfirmasi' in text_lower:
                    button_konfirmasi = button
        if button_2x and button_konfirmasi:
            if not is_2x_clicked:
                print(f"Pesan terupdate! Menemukan tombol '{button_2x.text}' dan '{button_konfirmasi.text}'")
                print(f"Mengklik tombol '{JUMLAH_PESANAN_STR}'...")
                try:
                    await button_2x.click()
                except Exception:
                    pass
            else:
                print(f"Pesan terupdate! Tombol '{JUMLAH_PESANAN_STR}' sudah bercentang ({button_2x.text}).")
                print("Mengklik tombol 'konfirmasi'...")
                try:
                    await button_konfirmasi.click()
                    print("Berhasil mengklik konfirmasi!")
                except Exception:
                    pass

async def main():
    print("Memulai client...")
    await client.start()
    print(f"Berhasil login (menggunakan notif.session). Memantau pesan dari {TARGET_BOT}...")
    await client.run_until_disconnected()

if __name__ == '__main__':
    asyncio.run(main())
