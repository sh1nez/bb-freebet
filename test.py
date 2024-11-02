import re

text = "qb1\n"  # Пример текста
regex = r'(?<!\S)[a-zA-Z0-9]{1,3}(?!\S)'  # Регулярное выражение, включая цифры

matches = re.findall(regex, text)  # Найти совпадения

if matches:
    print(matches)  # Вывод: ['ab1', 'a', 'b', 'c', 'd', 'e', 'fg', 'h', 'ij', 'kl', 'mn', 'op', 'qr', 'st']
