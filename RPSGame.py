import random

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
game_images = [rock, paper, scissors]
user_rps = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n"))
if user_rps >=3 or user_rps < 0: #makes sure num is between 0-2
    print("Invalid Num, You lose")
else:
    print(game_images[user_rps])

comp_pick = random.randint(0,2)#can only be within 0-2 due to the choices, genterates random num
print(f"Computer chose:")
print(game_images[comp_pick])

#test cases for the game.
if user_rps ==0 and comp_pick == 2:
    print("You Win!")
elif comp_pick ==  0 and user_rps == 2:
    print("You lose!")
elif comp_pick > user_rps:
    print("You lose!")
elif user_rps > comp_pick:
    print("You win!")
elif comp_pick == user_rps:
    print("It\'s a draw!")

    