from hangman_art import logo, dude_so_far
from words import random_word

def replace_blanks(letter):
  for i in range(len(word_so_far)):
    if random_word[i] == letter:
      word_so_far[i] = letter

# Create blanks for the letters
word_so_far = ["_"] * len(random_word)
num_of_guesses = 0

print(logo)
print(f"The word has {len(random_word)} letters.")
print(dude_so_far[num_of_guesses])
print(" ".join(word_so_far))

while num_of_guesses < 6 and "_" in word_so_far:
  guessed_letter = input("Guess a letter: ").lower()
  if guessed_letter in word_so_far:
    print("You already guessed that letter. Try again")
  elif guessed_letter in random_word:
    # replace blanks with letter in appropriate spots
    replace_blanks(guessed_letter)
    print("Good job! Keep going")
  else:
    print("Sorry, that letter is not in the word. You are one step closer to death.")
    num_of_guesses +=1
  print(dude_so_far[num_of_guesses])
  print(" ".join(word_so_far))
  print()

if "_" not in word_so_far:
  print("Congratulations! You won!")
else:
  print("YOU DIED.")
print(f"The word was {random_word}")


