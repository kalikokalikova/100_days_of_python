alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encode(message, shift):
  encoded_message = ""
  for l in message:
    new_l_code = alphabet.index(l) + shift
    if new_l_code > 25:
      new_l_code = new_l_code - 26
    encoded_message += alphabet[new_l_code]
  return encoded_message

def decode(message, shift):
  decoded_message = ""
  for l in message:
    new_l_code = alphabet.index(l) - shift
    if new_l_code < 0:
      new_l_code = new_l_code + 26
    decoded_message += alphabet[new_l_code]
  return decoded_message

command = input("Type 'encode' to encrypt, type 'decode' to decrypt: ")

if command == "encode":
  message_to_encode = input("Type your message: ")
  # remove spaces, lower case
  message_to_encode = list(message_to_encode.replace(" ","").lower())
  shift_number = int(input("Type your shift number: ")) # TODO deal with 23> shift input
  # do shift
  encoded_message = encode(message_to_encode, shift_number)
  print(f"Your encoded message is: {encoded_message}")
elif command == "decode":
  message_to_decode = input("Type your message to decode: ")
  shift_number = int(input("Type your shift number: "))
  decoded_message = decode(message_to_decode, shift_number)
  print(f"Your decoded message is: {decoded_message}")
else:
  print("That's not a thing. Please try again.")
