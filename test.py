import re
text = """Вот такую решил дать. Что думаете?

Фриха: ZASPIRIT*** - вставляйте KEKW

Активировать"""
words = re.findall(r'(?!PP)[a-zA-Z*]{4,}', text)

print(words)
