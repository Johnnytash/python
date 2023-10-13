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
import random

Choices = [rock, paper, scissors]
player = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
while player not in ['0', '1', '2']:
    print("Invalid input. Please enter 0, 1, or 2.")
    player = input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n")

player= int(player)
print(f"You chose:\n{Choices[player]}")

computer_choice = random.randint(0, 2)
print("Computer chose:")
print(Choices[computer_choice])

# Rock wins against scissors.rock = 0
# Scissors win against paper.paper = 1
# Paper wins against rock.scissors =2

if player >= 3 or player < 0:
    print("You chose an invalid choice You lose!")
elif player == 0 and computer_choice == 2:
    print("You win!")
elif player == 1 and computer_choice == 2:
    print("Computer Wins")
elif player == 2 and computer_choice == 1:
    print("You win!") 
elif player ==  2 and computer_choice == 0:
    print("Computer Wins")
elif player == computer_choice:
    print("It's a Draw")    
