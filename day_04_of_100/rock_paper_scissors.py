rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
from random import randint
options = [rock,paper,scissors]
your_score = 0
computer_score = 0
print("Welcome to rock paper scissors")
while True:

  computer_choice = randint(0,len(options)-1)
  person_choice  = int(input ("choose 1 for Rock, 2 for Paper, 3 for scissors\n")) -1
  if person_choice < len(options) and person_choice >= 0 :
    if person_choice == computer_choice:
      print("its a draw")
    elif person_choice == 0 and computer_choice ==2:
      your_score +=1
      print("You win ")
    elif person_choice == 1 and computer_choice ==0:
      your_score +=1
      print("You win ")  
    elif person_choice == 2 and computer_choice ==1:
      your_score +=1
      print("You win ")
      
    else:
      computer_score +=1
      print("You lose ")

    print(f"Score  you {your_score} : {computer_score} Computer")  
    print("You chose :") 
    print(options[person_choice])
    print("Computer chose :") 
    print(options[computer_choice])
  else:
    print("enter a valid option")
  play_again = input("do you want to play again ? yes? or no?").lower()

  if play_again.count("n") >=1:
    break
