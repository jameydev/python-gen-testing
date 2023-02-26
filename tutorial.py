import sys
import math
import random
import threading
import time
from functools import reduce


'''
Mathematical and Radical
'''
def quick_maths():
    print("5 + 2 = ", 5 + 2) # 5 + 2 = 7
    print("2^3 = ", 2 ** 3) # 2^3 = 8
    print("sqrt(16) = ", math.sqrt(16)) # sqrt(16) = 4

    print("Random ", random.randint(1, 100))

    print(math.inf) # literally prints inf ... LOL

    # nan
    print(math.inf - math.inf) # bruh... why?

'''
Output formatting
'''
def output_demo():
    print(12, 25, 2020, sep='/') # A Merry COVID-mas
    print("No newline", end='')
    print("\n%03d %s %.2f %c" %(2, "Jamey", 2.345, 'B')) # 002 Jamey 2.35 B

'''
Data type demonstration
'''
def data_types():
    v1 = (
            1 + 2
            + 3
    )  # weird, but a thing you can do

    print(v1)  # output: 6

    print(type(v1))  # an integer

    print(sys.maxsize)  # huge number

    # Floating point
    print(sys.float_info.max)  # big boi

    my_float = 2.75
    print(my_float)

    # Complex numbers
    z = 5 + 6j

    # Boolean
    is_thing = False

    if not is_thing:
        print("Not a thing... maybe it's stuff?")

    # Strings
    str1 = "Bruh, why?"
    str2 = '''TRIPLE QUOTED'''
    str3 = f"Formatted... {str1}"
    print(str3)
    print(str2)

    # Casting
    thing = 5.4
    print("Cast ", type(int(thing))) # 5
    print("Cast ", type(str(thing))) # "5.4"
    print("Cast ", type(chr(97)))
    print("Cast ", type(ord('a')))




'''
main function to hold all the things!!
'''
def main():
    print("Welcome to the python party!")
    name = input("What is your name? ")
    print(f"Hello, {name}! You're a pro developer now.")
    data_types()
    output_demo()
    quick_maths()