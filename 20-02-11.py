import random

t= int(input("반복값"))
e = 0

for i in range(t):
    if random.randint(1,6) ==2:
        e = e + 1


print(e / t)
