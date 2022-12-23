print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#Write your code below this line 👇
print("welcome to my Trasure Island\nYou\'re mission is to loacate the treasure !!")
answer = input("You are at a crossroad what direction do you take. Left? or Right?")
answer = answer.lower()

if answer.count("l") ==1:
  answer = input("You get to the river and no boat yet, do you, Wait? or Swim?").lower()
  if answer.count("w") ==1:
    answer = input("You safely get across the river to land where you see a red, green and blue door\nWhich do you take? Red, Green, Blue").lower()
    if answer.count("r") ==1:
      print("Congratulations You found my little red velvet cake ")
    elif answer.count("g") ==1:
      print("Game over My Dobberman chased you")
    elif answer.count("b") ==1:
      print("Game over you disappeared ")
    else:
      print("Tried to play smart?, you\'re DEAD '")
  else:
     print("Game Over you drowned in the river")
    
else:
  print("Game Over you fell into a hole")