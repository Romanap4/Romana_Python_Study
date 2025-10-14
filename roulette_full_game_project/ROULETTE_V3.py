import random

number = random.randint(0, 36)

def roulette(number):
    match number:
        case 1 | 3 | 5 | 7 | 9 | 12 | 14 | 16 | 18 | 19 | 21 | 23 | 25 | 27 | 30 | 32 | 34 | 36:
            return number, "red"
        case 2 | 4 | 6 | 8 | 10 | 11 | 13 | 15 | 17 | 20 | 22 | 24 | 26 | 28 | 29 | 31 | 33 | 35:
            return number, "black"
        case 0:
            return number, "green"

print(roulette(number))
