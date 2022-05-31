#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
inisen = "Last digit of {}".format(number)
if number < 0:
    lastdig = abs(number) % 10
    if lastdig == 0:
        medsen = "is {}".format(lastdig)
    else:
        medsen = "is -{}".format(lastdig)
    lastdig = lastdig * -1
else:
    lastdig = abs(number) % 10
    medsen = "is {}".format(lastdig)
if lastdig > 5:
    print("{} {} and is greater than 5".format(inisen, medsen))
elif lastdig == 0:
    print("{} {} and is 0".format(inisen, medsen))
elif lastdig < 6:
    print("{} {} and is less than 6 and not 0".format(inisen, medsen))
