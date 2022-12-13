import re
text = "kasfjdlksjd @aksjdf https://ksjflasjkdf"
url_pattern = re.compile(r"https?://\S+")
text = url_pattern.sub("", text)
tag_pattern = re.compile(r'@\w+')
text = tag_pattern.sub("", text)
print(text)

