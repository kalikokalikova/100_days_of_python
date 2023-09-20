import random

paper_image = """
  .--""--.___.._
 (  <__>  )     `-.
 |`--..--'|      <|
 |       :|       /
 |       :|--""-./
 `.__  __;' o!O
     ""
"""

rock_image = """
       ,--.--._
------" _, \___)
        / _/____)
        \//(____)
------\     (__)
       `-----"
"""

scissors_image = """

   _       ,/'
  (_).  ,/'
   _  ::
  (_)'  `\.
           `\.
"""

user_choice = input("What do you choose? Rock, paper, or scissors? ").lower()
computer_choice = random.choice(["rock", "paper", "scissors"])
choice_image_dict = { "rock":rock_image, "paper": paper_image, "scissors":scissors_image }

print("You chose "+user_choice)
print(choice_image_dict[user_choice])
print("The computer chose "+computer_choice)
print(choice_image_dict[computer_choice])

if user_choice == computer_choice:
  print("it's a tie! Play again!")
elif user_choice == "rock":
  if computer_choice == "scissors":
    print("You win!")
  else:
    print("You lose!")
elif user_choice == "scissors":
  if computer_choice == "paper":
    print("You  win!")
  else:
    print("You lose.")
elif user_choice == "paper":
  if computer_choice == "rock":
    print("You win!")
  else:
    print("You lose.")
else:
  print("Something's gone wrong. Please try again.")
