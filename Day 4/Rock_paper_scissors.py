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

#import random module 
import random

#INPUT either rock paper scissors with numerical value 

player_1 = int(input("Player 1, what would you like to choose: 0 = rock, 1 = paper, or 2 = scissors? \n"))

#choices in a list for ramdomization
choices = [rock,paper,scissors]


#Computer choice 
computer = random.randint(0,2)
computer_choice = choices[computer]


print(f"Player 1:\n{choices[player_1]} \n \n Computer: \n{computer_choice}")


#IF player 1 and computer values are the same, it's a tie
if player_1 == computer :
    print("IT'S A TIE!")
#ELIF player 1 picks rock and computer picks scissor
elif player_1 == 0 and computer == 2:
    print("YOU WIN!")
#ELIF player 1 is paper and computer is rock, you win
elif player_1 == 1 and computer == 0:
    print("YOU WIN!")
#elif player picks scissors and computer picks paper , you win
elif player_1 == 2 and computer == 1:
    print("YOU WIN!")
#ELSE you lose
else:
    print("YOU LOSE!")



