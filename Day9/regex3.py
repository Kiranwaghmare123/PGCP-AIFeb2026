import re

text = input("Enter text")

result = re.sub(r"\s","-", text)

print(result)