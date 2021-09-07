#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last = "Last digit of"
lastnum = number%10
if lastnum > 5:
    print("{2} {0} is {1} and is greater than 5".format(number, lastnum, last))
elif lastnum == 0:
    print("{2} {0} is {1} and is 0".format(number, lastnum, last))
else:
    print("{2} {0} is {1} and is less than 6 and not 0".format(number, lastnum, last)) 
