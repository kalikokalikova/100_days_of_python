import nltk
import random

# Get the random word
nltk.download('words') # Download the words corpus (if you haven't already)
from nltk.corpus import words # Import the words corpus
english_words = words.words() # Get a list of English words
short_words = [word for word in english_words if len(word) <= 10] # Filter words that are 10 letters or less
random_word = random.choice(short_words) # Get a random word from the filtered list
random_word.lower