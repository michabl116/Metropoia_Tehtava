import random

def noppa():
    return random.randint(1, 6)

silmaluku = 0
while silmaluku != 6:
    silmaluku = noppa()
    print(f"Heiton tulos: {silmaluku}")