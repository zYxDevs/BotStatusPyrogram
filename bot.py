from asyncio import sleep
from pyrogram import Client
from pyrogram.errors import FloodWait
from config import API_HASH, API_ID, SUPPORT_ID, SESSION_NAME

app = Client(
    name="restartub",
    session_string=SESSION_NAME,
    api_id=API_ID,
    api_hash=API_HASH,
)


async def main():
    async with app:
        while True:
            print("Starting!")
            try:
                await app.send_message(SUPPORT_ID, "/restart")
                await sleep(10)
                await app.send_message(SUPPORT_ID, "/remdump")
            except FloodWait as e:
                await sleep(e.x)
            return print("Complete!")


app.run(main())
