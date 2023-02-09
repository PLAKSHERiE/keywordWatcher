from pyrogram import Client

from config import API_ID, API_HASH, DEVICE_MODEL, SYSTEM_VERSION, APP_VERSION, PHONE, PASSWORD

app = Client(
    f'accs/{PHONE}',
    api_id=API_ID,
    api_hash=API_HASH,
    device_model=DEVICE_MODEL,
    system_version=SYSTEM_VERSION,
    app_version=APP_VERSION,
    phone_number=PHONE,
    password=PASSWORD
)

