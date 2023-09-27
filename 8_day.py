alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(message, shift, shift_direction):
  if shift_direction == "decode":
    shift *= -1
  result = ""
  for char in message:
    shifted_char_index = (alphabet.index(char) + shift) % 26
    result += alphabet[shifted_char_index]
  return result

session_active = True

while session_active:
  command = input("Type 'encode' to encrypt, type 'decode' to decrypt: ")
  message = input("Type your message: ")
  message = list(message.replace(" ","").lower())
  shift_number = int(input("Type your shift number: "))
  shifted_message = caesar(message, shift_number, command)
  print(f"Your {command}d message is: {shifted_message}\n")
  keep_going = input("Would you like to have another go? Type 'yes' or 'no': ")
  print()
  session_active = bool(keep_going == "yes")

