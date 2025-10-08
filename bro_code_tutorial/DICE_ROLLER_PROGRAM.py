import random

# print("\u25CF \u250C \u2500 \u2510 \u2502 \u2514 \u2518")   # entering unicode characters in Python
                                                              # print the characters, copy into a comment and the line above can be deleted           
# ● ┌ ─ ┐ │ └ ┘
# building ASCII art:

"┌─────────┐"
"│         │"
"│         │"
"│         │"
"└─────────┘"

dice_art = {
    1: ("┌─────────┐", 
        "│         │", 
        "│    ●    │", 
        "│         │", 
        "└─────────┘"),
    2: ("┌─────────┐", 
        "│  ●      │", 
        "│         │", 
        "│      ●  │", 
        "└─────────┘"),
    3: ("┌─────────┐", 
        "│  ●      │", 
        "│    ●    │", 
        "│      ●  │", 
        "└─────────┘"),
    4: ("┌─────────┐", 
        "│  ●   ●  │", 
        "│         │", 
        "│  ●   ●  │", 
        "└─────────┘"),
    5: ("┌─────────┐", 
        "│  ●   ●  │", 
        "│    ●    │", 
        "│  ●   ●  │", 
        "└─────────┘"),
    6: ("┌─────────┐", 
        "│  ●   ●  │", 
        "│  ●   ●  │", 
        "│  ●   ●  │", 
        "└─────────┘")    
}

dice = []
total = 0
num_of_dice = int(input("How many dice?:  "))

for die in range(num_of_dice):
    dice.append(random.randint(1, 6))

# for die in range(num_of_dice):
#     for line in dice_art.get(dice[die]):
#         print(line)

# if you want the dice lined up next to each other:

for line in range(5):
    for die in dice:
        print(dice_art.get(die)[line], end="")       #????? figure it out later - figured it out right away, it was one wrong digit T_T
    print()

for die in dice:
    total += die
print(f"total: {total}")
