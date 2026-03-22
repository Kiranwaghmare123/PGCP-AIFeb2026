import datetime
#age calculator

birthdate = datetime.date(2000, 5,10)

today = datetime.date.today()

age_days = today - birthdate

age_years = age_days // 365

print("Age: ",age_years, "Years")
