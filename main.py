alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

####CHARACTER SHIFTING
def caesar(start_text, shift_amount, cipher_direction):
  end_text = ""
  if cipher_direction == "decode":
    shift_amount *= -1
  for char in start_text:
    if char in alphabet:
        position = alphabet.index(char)
        new_position = position + shift_amount
        end_text += alphabet[new_position]
    else:
        end_text += char

#####RESULT  
  print(f"Here's the {cipher_direction}d secret: {end_text}")

####LOGO HEADER
from logo import caesar_logo
print(caesar_logo)
print("                                       𝟸𝟶𝟸𝟶 | @𝙲𝚖𝚕𝚘𝚑𝚛")
print("---------------------------------------------------------------------------------------------")

####CONTINUE PROGRAM WHILE LOOP
should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 25

    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

    result = input("Type 'yes' to continue.  Type 'no' to close.\n").lower()
    if result == "no":
        should_continue = False
        print("Goodbye")