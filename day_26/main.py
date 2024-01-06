import pandas

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

phonetic_df = pandas.read_csv("nato_phonetic_alphabet.csv")
phonetic_dict = {row.letter:row.code for (index, row) in phonetic_df.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
word_to_encode = input("Please give me a word to encode: ").upper()
code = [phonetic_dict[letter] for letter in word_to_encode]

print(code)
