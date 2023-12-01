import random

def play_game():
    # welcome and choose easy or hard
    easy_or_hard = input("Let's play a guessing game. I've chosen a number between 1 and 100. Do you want to play the easy or the hard version? ")

    # if easy set numebr of tries to 10, else 5
    number_of_tries = 10 if easy_or_hard == 'easy' else 5

    # choose random number between 1 and 100
    target_number = random.randint(1,100)
    guessed_number = 0
    winner = False

    # if the number of tries is greater than 0, keep guessing
    while number_of_tries > 0 and not winner:
    # input a guess
        guessed_number = int(input("Guess a number: "))
        winner = check_guess(guessed_number, target_number)
        number_of_tries -= 1

    if not winner:
        print(f"Sorry, you lose. The number was {target_number}")

def check_guess(guessed_number, target_number):
    # determine whether the guessed number is higher, lower, or exactly the target number
    if guessed_number == target_number:
        print(f"You got it! The number was {target_number}")
    elif guessed_number > target_number:
        print("Too high")
    elif guessed_number < target_number:
        print("Too low.")
    return guessed_number == target_number

play_game()


