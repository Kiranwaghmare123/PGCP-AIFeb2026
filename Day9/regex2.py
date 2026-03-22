import re

text = input("Enter mobile number")

if re.fullmatch(r"[6-9]\d{9}",text):
    print("Correct !!!")
else:
    print("Not correct")