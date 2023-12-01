import random

def fizzbuzz(number):

  for n in range(1,number+1):
    if n % 15 == 0:
      print("fizzbuzz")
    elif n % 5 == 0:
      print("buzz")
    elif n % 3 == 0:
      print("fizz")
    else:
      print(n)


# character = chr(ascii_code)
# letter = chr(65) => letter = "A"

def passwordGenerator():
  letters = int(input("How many letters would you like in your password? "))
  symbols = int(input("How many symbols would you like? "))
  numbers = int(input("How many numbers would you like? "))

  pw_list = []

  for _ in range(0,letters):
    letter = chr(random.randint(65, 90)) # ascii 65 - 90 uppercase letters
    is_lowercase = random.choice([True, False])
    if is_lowercase:
      letter = letter.lower()
    pw_list.append(letter)

  for _ in range(0, symbols):
    symbol = chr(random.randint(33,38)) # ascii 33 - 38 symbols
    pw_list.append(symbol)

  for _ in range(0, numbers):
    pw_list.append(str(random.randint(0,9)))

  random.shuffle(pw_list)
  return "".join(pw_list)


print(passwordGenerator())

