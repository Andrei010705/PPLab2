import random

print("Aici e coul python: ")

def gen():
    v = []
    for _ in range(20):
        x = random.randint(0, 9999999)
        print(x)
        v.append(x)
    return v

lista = gen()
lista