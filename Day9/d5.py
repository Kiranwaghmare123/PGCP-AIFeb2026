import datetime

date_str = "25-03-2026"

date = datetime.datetime.strptime(date_str, "%d-%m-%Y").date()

print(date)