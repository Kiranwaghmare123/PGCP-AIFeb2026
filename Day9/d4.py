import datetime

deadline = datetime.date(2026, 3,26)

today = datetime.date.today()

if today > deadline:
    print("deadline : over")
elif today == deadline:
    print("deadline = today")
else:
    print("DEadline : yet to reach")
    