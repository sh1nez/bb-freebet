import re


def find_hints(text):
    matches = re.findall(r'(?!.*\*)"([A-Z]+)"', text)
    if len(matches) == 1:
        return matches

    matches = re.findall(r'\b(?!.*\*)[A-Z]+\b', text)

    if matches:
        return matches

    return []


text = """Вот такую решил дать. Что думаете?

Фриха: ZASPIRIT*** - вставляйте KEKW

Активировать"""
print(find_hints(text))
