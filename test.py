import re
import logging

# Настройка логирования
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def find_hint(text):
    matches = re.findall(r'"(.*?)"', text)
    if len(matches) == 1:
        logger.info(f"find hint: {matches[0]}")
        return matches[0]
    return None


# Пример использования
text1 = 'Это "единственное слово".'
text2 = 'Это "первое слово" и "второе слово".'
text3 = 'Нет слов в кавычках.'

print(find_hint(text1))  # Вернет: единственное слово
print(find_hint(text2))  # Вернет: None
print(find_hint(text3))  # Вернет: None
