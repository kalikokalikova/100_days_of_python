# open name file, put each line into a list
with open('./Input/Names/invited_names.txt') as name_file:
    names = name_file.read().splitlines()

# open letter body file, put content into variable
with open('./Input/Letters/starting_letter.txt') as letter_file:
    letter = letter_file.read()

# loop through list of names, replace [name] with actual name, save that to a new file
for name in names:
    new_letter = letter.replace('[name]', name)
    with open(f"./Output/ReadyToSend/{name}.txt", "w") as personalized_letter:
        personalized_letter.write(new_letter)
