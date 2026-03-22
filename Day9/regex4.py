import re
text = "Hello everyone, we have to implement python project"

words = re.findall(r"\b\w+\b", text)
print(len(words))