#  ┐ └ ┏ ┚

# dice basic blueprint:

#  ┏--------┓
#  ┃        ┃
#  ┃        ┃
#  ┃        ┃
#  ┗--------┛

import random

dice_dictionary= {
    1: (
     "┏---------┓",
     "┃         ┃",
     "┃    ●    ┃",
     "┃         ┃",
     "┗---------┛"
     ),
    2: (
     "┏---------┓",
     "┃ ●       ┃",
     "┃         ┃",
     "┃       ● ┃",
     "┗---------┛"
     ),
    3: (
     "┏---------┓",
     "┃  ●      ┃",
     "┃    ●    ┃",
     "┃      ●  ┃",
     "┗---------┛"
     ),
    4: (
     "┏---------┓",
     "┃ ●     ● ┃",
     "┃         ┃",
     "┃ ●     ● ┃",
     "┗---------┛"
     ),
    5: (
     "┏---------┓",
     "┃ ●     ● ┃",
     "┃    ●    ┃",
     "┃ ●     ● ┃",
     "┗---------┛"
     ),
    6: (
     "┏---------┓",
     "┃ ●  ●  ● ┃",
     "┃         ┃",
     "┃ ●  ●  ● ┃",
     "┗---------┛"
     ),
}

dice_roll= int(input("Enter the number of times you want the dice to be rolled: "))

totalChoice = []

choice= dice_roll >=1 and dice_roll <=6

while not choice:
    print("Please enter a number between 1 and 6")
    dice_roll= int(input("Enter the number of times you want the dice to be rolled: "))
    choice= dice_roll >=1 and dice_roll <=6


for i in range(dice_roll):
    tChoice= random.randint(1,6)
    totalChoice.append(tChoice)

for j in range(5):
    for k in totalChoice:
        print(dice_dictionary[k][j], end="")
    print()




# print(totalChoice)