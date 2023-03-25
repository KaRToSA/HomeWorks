import random

def gen_rand():
    while True:
        yield random.randint(1, 1000)

print(next(gen_rand()))

def gen_range(start,stop,step):
    number = start
    while number<stop:
        yield number
        number += step

def gen_enumerate(sequence, start=0):
    n = start
    for element in sequence:
        yield n, element
        n += 1
def gen_map(func,LisT):
    for i in LisT:
        yield func(i)
print(list(gen_map(lambda x:x+3,[1,2,62,62,23])))
print(list(gen_range(1,100,3)))

seasons = ['Spring', 'Summer', 'Fall', 'Winter']
print(list(gen_enumerate(seasons)))