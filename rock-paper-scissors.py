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

#Write your code below this line 👇
print("Rock, Paper, Scissors!")
user_choice = int(
    input(
        "What do you pick?(Type 0 for rock, 1 for paper and 2 for scissors)\n")
)

if user_choice == 0:
    print("You picked: rock" + rock)
elif user_choice == 1:
    print("You picked: paper" + paper)
else:
    print("You picked: scissors" + scissors)

comp_choice = random.randint(0, 2)
if comp_choice == 0:
    print("Computer picked: rock" + rock)
elif comp_choice == 1:
    print("Computer picked: paper" + paper)
else:
    print("Computer picked: scissors" + scissors)

if user_choice > 2 or user_choice < 0:
    print("Invalid choice!")
elif user_choice == 0 and comp_choice == 2:
    print("You win!")
elif comp_choice == 0 and user_choice == 2:
    print("You lose!")
elif comp_choice > user_choice:
    print("You lose!")
elif user_choice == comp_choice:
    print("It's a draw.")
else:
    print("You win!")
