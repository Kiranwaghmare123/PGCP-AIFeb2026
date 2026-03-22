import re

text = input("Enter string")

if re.fullmatch(r"[A-Za-z]+",text):
    print("Only alphabets !!!")
else:
    print("Not only characters")