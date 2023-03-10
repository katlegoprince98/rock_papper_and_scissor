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


comp = random.randint(1,3)
user = int(input("What do you choose, 1-for rock, 2-papper and 3-scissors"))
game_imga = [rock, paper, scissors]

if user > 2 or user < 0:
   print("Invalid choice")
else:
   print(game_imga[user])
   

if user == 0 and comp == 2:
  print(f"You chose {user} and the computer chose {comp}")
  print("You win")
  print(rock)
elif user == 2 and comp == 0:
  print(f"You chose {user} and the computer chose {comp}")
  print("You lose")
  print(rock)
elif user == 2 and comp == 1:
   print(f"You chose {user} and the computer chose {comp}")
   print("You win")
   print(scissors)
elif user == 1 and comp == 2:
   print(f"You chose {user} and the computer chose {comp}")
   print("You lose")
   print(scissors)
elif user == 1 and comp == 0:
   print(f"You chose {user} and the computer chose {comp}")
   print("You win")
   print(paper)
elif user == 0 and comp == 1:
   print(f"You chose {user} and the computer chose {comp}")
   print("You win")
   print(paper)
elif comp == user:
    print(f"You chose {user} and the computer chose {comp}")
    print("DRAW")
   
  
  
  

