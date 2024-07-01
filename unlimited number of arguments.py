#Anoushka Saha
#Day 27 Practice
#Intro to *args and **kwargs
#July 1st, 2024

def add(*args): 
    sum = 0
    for n in args:
        sum += n
    return sum

print(add(2, 4, 6))

def calculate(n, **kwargs):
    print(type(kwargs))
    #for key, value, in kwargs.items():
    #    print(key)
    #    print(value)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculate(2, add = 3, multiply = 5)