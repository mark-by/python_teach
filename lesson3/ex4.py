import datetime

day = int(input("day="))
month = int(input("month="))
year = int(input("year="))

birth = datetime.datetime(year=year, day=day, month=month)

today = datetime.datetime.now()

diff = today - birth

print(diff.days)
print(diff.seconds)
