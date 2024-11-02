from pyrogram import Client, types
from transcript import to_text
from datetime import datetime
import socket
import sys
import random
import re
import logging
import string

logger = logging.getLogger('freebet')

logging.basicConfig(
    # (DEBUG, INFO, WARNING, ERROR, CRITICAL)
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler()  # Вывод в консоль
        # logging.FileHandler('log.txt'),
    ]
)

name = "freebet"
app_id = 21907547
app_hash = "6f9ce40381033a9d9924430757cf6b07"
app = Client(name, api_id=app_id, api_hash=app_hash)

aunk = [-1001979310355, -1001810104257]
maxBet = [-1001525747974, -1001810104257]
channels = [-1001810104257,
            -1001525747974,
            -1001979310355, -1001889498592,]

name_cnt = 0

clients = []

logger.warning(sys.argv[1:])
for i in sys.argv[1:]:
    clients.append(("localhost", int(i)))

clients_len = len(clients)
assert clients_len != 0

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


def many_clients(promos):
    for i in clients:
        for p in promos:
            send(p, i)


def send(promo, client):
    logger.info(f"send promi {promo} to {client[1]}")
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
        a = to_text("downloads/" + name)
        logger.info(a)
        return a
    except Exception:
        return ""


def find_hints(text):
    matches = re.findall(r'(?!.*\*)"([A-Z]+)"', text)

    if len(matches) == 1:
        logger.debug(f"find hint {matches[0]}")
        return matches

    matches = re.findall(r'\b(?!.*\*)[A-Z]+\b', text)

    if matches:
        logger.debug(f"find hints {' '.join(matches)}")
        return matches

    return []


def replace(words, hints=None):
    logger.info(f"replace start: {' '.join(words)}")
    new = []
    if hints:
        for w in words:
            for h in hints:
                new.append(re.sub(r'\*+', h, w))
    else:
        for h in words:
            if "*" in h:
                if h.count("*") != 1:
                    continue
                else:
                    for w in string.digits + string.ascii_uppercase:
                        new.append(h.replace("*", w))

    logger.info(f"replace end: {' '.join(new)}")
    return new


@app.on_message()
async def filter_messages(cli, message: types.Message):
    if message.chat.id not in channels:
        return
    media_text = ""
    text = ""
    words = []

    if message.__dict__["media"]:  # promi in pic
        media_text += await media_to_text(message)

    if message.__dict__['text']:
        text += message.text

    if message.__dict__['caption']:
        text += message.caption

    url_pattern = re.compile(r"https?://\S+")
    text = url_pattern.sub("", text)
    tag_pattern = re.compile(r'@\w+')
    text = tag_pattern.sub("", text)

    text += media_text
    pp_pattern = re.compile(r'PP.{8}', re.IGNORECASE)
    words = pp_pattern.findall(text)

    if words:  # PP*
        fl = any("*" in i for i in words)
        if message.chat.id in aunk:
            logger.debug("aunk PP")
            if fl:
                many_clients(replace(words, ["WW"]))
            else:
                many_promos(words)
        else:  # max
            logger.debug("max PP")
            if fl:
                hints = find_hints(text)
                many_clients(replace(words, hints))
            many_promos(words)
    else:  # if not PP*
        words = re.findall(r'(?!PP)[a-zA-Z0-9*]{5,}', text)
        fl = any("*" in i for i in words)
        if message.chat.id in aunk:
            logger.debug("aunk !PP")
            if fl:
                tmp = [i for i in words if "*" in i]
                many_clients(replace(words, ["WW"]))
            else:
                many_promos(words)
        else:
            logger.debug(f"max !PP{message.chat.id}")
            if fl:
                hints = find_hints(text)
                # tmp = [i for i in words if "*" in i]
                many_clients(replace(words, hints))
            many_promos(words)


logger.warning("start!")
app.run()
