alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',' ']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


letter_indexes =[]

def caesar(_text,_shift,_direction):
  global alphabet
  cipher_text = ""
  for letter in _text:
      letter_indexes.append(alphabet.index(letter))
  for index in range(len(letter_indexes)):
    if _direction == "encode":
      letter_indexes[index] += _shift
    elif direction == "decode":
      letter_indexes[index] -= _shift
    # else:
    #   return "opps!, sorry, enter a valid command "  
  for index in range (len(_text)):
    if letter_indexes[index] > len(alphabet) -1:
       letter_indexes[index] = letter_indexes[index] % len(alphabet)
    cipher_text += alphabet[letter_indexes[index]]
  return cipher_text    

print(f"your ciphered text is {caesar(_text=text,_shift=shift,_direction=direction)}")    