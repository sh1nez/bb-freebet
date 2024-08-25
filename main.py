from pyrogram import Client, types
from transcript import to_text
from stealth import promo
from datetime import datetime
import random
import re
import logging

logger = logging.getLogger('my_logger')

logging.basicConfig(
    # (DEBUG, INFO, WARNING, ERROR, CRITICAL)
    level=logging.WARNING,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('log.txt'),
        # logging.StreamHandler()  # Вывод в консоль
    ]
)

name = "freebet"

app = Client(name)

channels = ["-1001755139624", "-1001889498592",
            "-1001810104257", "-1001525747974", "-1001979310355"]


name_cnt = 0


@app.on_message()
async def filter_messages(cli, message: types.Message):
    if str(message.chat.id) not in channels:
        return
    words = []
    if message.__dict__["media"]:
        global name_cnt
        name_cnt += 1
        try:
            name = datetime.now().strftime('%Y-%m-%d %H:%M:%S') + \
                str(name_cnt) + ".jpg"
            if name_cnt > 9:
                name_cnt = 0
            await message.download(name)
            words = to_text("downloads/" + name)
        except Exception:
            # continue
            pass

    string = None
    if message.__dict__['text']:
        words.extend(message.text.split())
        string = message.__dict__['text']

    if message.__dict__['caption']:
        words.extend(message.caption.split())
        string = message.__dict__['caption']

    new = []
    for i in words:
        if "PP" in i:
            inx = i.find("PP")
            new.append(i[inx:10])

    words = new

    if not words:
        if not string:
            return
        url_pattern = re.compile(r"https?://\S+")
        string = url_pattern.sub("", string)
        words = re.findall(r'\b[a-zA-Z0-9]{10,}\b', string)
        if not words:
            return
    else:
        print(datetime.now().strftime('%H:%M:%S'), "triggered")
        print("using promo...")
    random.shuffle(words)
    for i in words:
        promo(i)


logger.warning("start!")

app.run()
