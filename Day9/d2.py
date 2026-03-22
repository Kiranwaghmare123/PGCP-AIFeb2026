import datetime

d1 = datetime.date(2026, 3, 21)
d2 = datetime.date(2026, 5, 15)

diff = d2 - d1
print(diff)

today = datetime.date.today()
f1 = today +  datetime.timedelta(days=5)
print(f1)


f2= today -  datetime.timedelta(days=5)
print(f2)