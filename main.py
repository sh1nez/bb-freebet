from transcript import to_text
from stealth import promo
from pyrogram import Client, filters, types
from datetime import datetime
import random

name = "freebet"

app = Client(name)

channels = ["-1001755139624", "-1001889498592",
            "-1001810104257", "-1001525747974", "-1001979310355"]


@app.on_message()
async def filter_messages(cli, message: types.Message):
    if str(message.chat.id) not in channels:
        return
    print(datetime.now().strftime('%H:%M:%S'), "triggered")
    words = []
    if message.__dict__["media"]:
        try:
            name = datetime.now().strftime('%Y-%m-%d %H:%M:%S') + ".jpg"
            await message.download(name)
            words = to_text("downloads/" + name)
        except Exception:
            pass

    if message.__dict__['text']:
        words.extend(message.text.split())

    if message.__dict__['caption']:
        words.extend(message.caption.split())

    new = []
    print("check promo")
    for i in words:
        if "PP" in i:
            inx = i.find("PP")
            new.append(i[inx:10])
    words = new
    if not words:
        return
    else:
        print("using promo...")
    random.shuffle(words)
    for i in words:
        promo(i)

app.run()
