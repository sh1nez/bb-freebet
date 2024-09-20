import re
import logging


def replace(words, hint=None):
    new = []
    if hint:
        for v in words:
            pattern = r'\*+'
            new.append(re.sub(r'\*+', hint, v))

    else:
        for i in words:
            if "*" in i:
                if i.count("*") != 1:
                    continue
    words = new
    return words


# Настройка логирования
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def find_hint(text):
    matches = re.findall(r'"(.*?)"', text)
    if len(matches) == 1:
        logger.info(f"find hint: {matches[0]}")
        return matches[0]
    return None


words = replace(["wpqerpwe*1", "asdfasd**1"], "T")

for i in words:
    print(i)
