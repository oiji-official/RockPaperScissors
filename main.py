rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
print("Rule:\n Play 1 for Rock;\n Play 2 for Paper;\n Play 3 for Scissors")
user = input("Rock, Paper, Scissors!\n")
import random

computer = random.randint(1,3)

row1 = ["Draw", "You Win!", "You Lose T_T"]
row2 = ["You Lose T_T", "Draw", "You Win!"]
row3 = ["You Win!", "You Lose T_T", "Draw"]
matrix = []
matrix.append(row1)
matrix.append(row2)
matrix.append(row3)

art = [rock, paper, scissors]
print(art[int(user) - 1])
print("Computer chose~")
print(art[int(computer) - 1])
row = int(user) - 1
column = int(computer) - 1
# print(row)
# print(column)

test = matrix[column][row]
print(test)
