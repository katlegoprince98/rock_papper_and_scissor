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

if user == 1 and comp == 3:
  print(f"You chose {user} and the computer chose {comp}")
  print("You win")
  print(rock)
elif user == 3 and comp == 1:
  print(f"You chose {user} and the computer chose {comp}")
  print("You lose")
  print(rock)
elif user == 3 and comp == 2:
   print(f"You chose {user} and the computer chose {comp}")
   print("You win")
   print(scissors)
elif user == 2 and comp == 3:
   print(f"You chose {user} and the computer chose {comp}")
   print("You lose")
   print(scissors)
elif user == 2 and comp == 1:
   print(f"You chose {user} and the computer chose {comp}")
   print("You win")
   print(paper)
elif user == 1 and comp == 2:
   print(f"You chose {user} and the computer chose {comp}")
   print("You win")
   print(paper)
elif comp == user:
    print(f"You chose {user} and the computer chose {comp}")
    print("DRAW")
   
  
  
  

