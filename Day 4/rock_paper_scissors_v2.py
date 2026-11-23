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
#list of valid numbers 
valid_numbers = [0, 1, 2]

#Computer choice 
computer = random.randint(0,2)
#removed computer_choice variable as it was not needed. Added it to the print line
#learned something new : not in for lists. If player_1 value is NOT IN valid number list, this will be my defauly deny
if player_1 not in valid_numbers:
    print("Please pick a number from 0, 1, or 2 and try again.")
else:
    print(f"Player 1:\n{choices[player_1]} \n \n Computer: \n{choices[computer]}")
    #IF player 1 and computer values are the same, it's a tie
    if player_1 == computer :
        print("IT'S A TIE!")
    #ELIF player1's choice minus computers choice divided by 3 with a remainder of 1 = win 
    elif (player_1 - computer)%3 ==1 :
        print("YOU WIN!")
    #ELSE you lose
    else:
        print("YOU LOSE!")

# Fix: Created a list of valid numbers so that if the input value for player 1 is not in the list, it returns an 
#error message. I also indented all other conditions under else so that none of the conditions would be considered 
#until it passes the first check 