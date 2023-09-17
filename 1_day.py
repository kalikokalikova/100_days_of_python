def pluralize(word):
  if word[-1] == 's':
    return word+"es"
  else:
    return word+"s"

print("Welcome to Band Name Generator.")
place_name = input("What's the name of the place where you grew up? ")
pet_name = input("What's the name of your pet? ")
pet_name = pluralize(pet_name)

print(f"Your band name could be The {place_name} {pet_name}")


