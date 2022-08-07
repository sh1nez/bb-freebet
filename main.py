from pyrogram import Client, types
from transcript import to_text
from datetime import datetime
import socket
import sys
import random
import re
import logging

logger = logging.getLogger('freebet')

logging.basicConfig(
    # (DEBUG, INFO, WARNING, ERROR, CRITICAL)
    level=logging.WARNING,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        # logging.StreamHandler()  # Вывод в консоль
        logging.FileHandler('log.txt'),
    ]
)

name = "freebet"
app_id = 21907547
app_hash = "6f9ce40381033a9d9924430757cf6b07"
app = Client(name, api_id = app_id, api_hash = app_hash)

channels = ["-1001755139624", "-1001889498592",
            "-1001810104257", "-1001525747974", "-1001979310355"]

name_cnt = 0

clients = []

logger.warning(sys.argv[1:])
for i in sys.argv[1:]:
    clients.append(("localhost", int(i)))

clients_len = len(clients)
assert clients_len != 0

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


def many_clents(promo):
    for i in clients:
        send(promo, i)


def send(promo, client):
    logger.warning(f"send promi {promo} to {client[1]}")
    promo += "<END>"
    sock.sendto(promo.encode("utf-8"), client)


def many_promos(arr: [str]):
    random.shuffle(clients)
    for i, promo in enumerate(arr):
        send(promo, clients[i % clients_len])


async def media_to_text(message: types.Message):
    global name_cnt
    name_cnt += 1
    try:
        name = datetime.now().strftime('%Y-%m-%d %H:%M:%S') + str(name_cnt) + ".jpg"
        if name_cnt > 9:
            name_cnt = 0
        await message.download(name)
        return to_text("downloads/" + name)
    except Exception:
        pass


@app.on_message()
async def filter_messages(cli, message: types.Message):
    if str(message.chat.id) not in channels:
        return
    words = []
    if message.__dict__["media"]:
        words = await media_to_text(message)

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
        if words:
            logger.warning("using promo...")
            for i in words:
                many_clents(i)
        return
    else:
        logger.warning("using promo...")
        many_promos(words)

logger.warning("start!")
app.run()
