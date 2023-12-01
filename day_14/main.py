from data import data
from art import logo, vs
import random
import os

def find_winner(choices):
    if choices[0]["follower_count"] > choices[1]["follower_count"]:
        return '1'
    else:
        return '2'

counter = 0

still_winning = True
first_choice = random.choice(data)
while still_winning:
    print(logo)
    choices = [first_choice, random.choice(data)]
    # make sure we have two different objects
    while choices[0] == choices[1]:
        choices[1] = random.choice(data)
    winner = find_winner(choices)

    print("Who has more followers?")
    print(f"(1) {choices[0]['name']}, a {choices[0]['description']} from {choices[0]['country']}")
    print(vs)
    print(f"(2) {choices[1]['name']}, a {choices[1]['description']} from {choices[1]['country']}")
    guess = input("Please type '1' or '2': ")

    if guess == winner:
        os.system('clear')
        print("You are correct!!")
        counter += 1
        print(f"Your score is now {counter}\n")
        first_choice = choices[int(winner)-1]
    else:
        still_winning = False

# express condolences
print("Sorry, you lost")
print(f"Your score is {counter}")


