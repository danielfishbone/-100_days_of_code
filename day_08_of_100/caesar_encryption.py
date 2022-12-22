alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',' ']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


letter_indexes =[]

def encrypt(_text,_shift):
  global alphabet
  encrypted_text = ""
  for letter in _text:
          letter_indexes.append(alphabet.index(letter))
  for index in range(len(letter_indexes)):
    letter_indexes[index] += _shift
  for index in range (len(_text)):
    if letter_indexes[index] > len(alphabet) -1:
       letter_indexes[index] = letter_indexes[index] % len(alphabet)
    encrypted_text += alphabet[letter_indexes[index]]
  return encrypted_text    
    
def decrypt(_text,_shift):
  global alphabet
  decrypted_text =""
  for letter in _text:
          letter_indexes.append(alphabet.index(letter))
  for index in range(len(letter_indexes)):
    letter_indexes[index] -= _shift
  for index in range (len(_text)):
    if letter_indexes[index] > len(alphabet) -1:
       letter_indexes[index] = letter_indexes[index] % len(alphabet)
    decrypted_text += alphabet[letter_indexes[index]]
  return decrypted_text


if direction == "encode":
  print(f"your encrypted text is {encrypt(text,shift)}")
elif direction == "decode": 
  print(f"your decrypted text is {decrypt(text,shift)}")
else:
  print("opps!, sorry enter a valid command ")