import random

win_num = [[1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36], 
           [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35],
           [0]]

num = random.choice(random.choice(win_num))

if num in win_num[0]:
    print(f"{num}, red")
elif num in win_num[1]:
    print(f"{num}, black")
elif num in win_num[2]:
    print(f"{num}, green")


