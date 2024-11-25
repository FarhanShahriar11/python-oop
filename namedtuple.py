from collections import namedtuple
date=namedtuple('date',['month','day','year'])
yesterday=date(10,7,2024)
today=date(10,8,2024)
tomorrow=date(10,9,2024)
print(yesterday,today,tomorrow)
print(today.day)
print(tomorrow.year)
