# own modules
import fmath

fmath.add(1,2)
fmath.substract(1,2)

from fmath import add, substract

add(5,5)
substract(8,4)


# online modules https://pypi.org/
from colorama import init, Fore, Style

init(convert=True)
print("hello world")
print(Fore.RED + "hello world")


# python modules https://docs.python.org/es/3/py-modindex.html

import datetime
print(datetime.timedelta(minutes=100))

from datetime import timedelta, date

print(timedelta(minutes=100))
print(date.today())
