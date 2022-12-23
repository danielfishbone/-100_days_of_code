import os

is_bidding =True
bidders = {}
highest_bid = 0
highest_bidder = ""
while is_bidding:
  name = input("What is your name?\n").capitalize()
  amount = int(input("How much are you bidding?\n"))
  bidders[name] = amount

  if input("Are there any more bidders?, yes or no\n").lower() == "no":
    is_bidding = False
  os.system('cls' if os.name == 'nt' else 'clear')    
for bidder in bidders:
  if bidders[bidder] > highest_bid:
     highest_bid = bidders[bidder]
     highest_bidder = bidder

print(f"{highest_bidder} Won with a ${highest_bid} bid")
    