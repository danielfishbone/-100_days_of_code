from random import choice 

player_cards = []
dealer_cards = []
player_stake = 0
player_cash  = 1000
player_score = 0
dealer_score = 0
cashout =False

def deal_card():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  return choice(cards)
def check_score(_player_cards,_dealer_cards):
    _player_score = 0
    _dealer_score = 0
    ace_flag = 0
    for card in _player_cards:
        if card == 11:
            ace_flag += 1
        _player_score += card
        while _player_score > 21 and ace_flag > 0:
            _player_score -= 10
            ace_flag -= 1
    ace_flag = 0
    for card in _dealer_cards:
        if card == 11:
            ace_flag += 1
        _dealer_score += card
        while _dealer_score > 21 and ace_flag > 0:
            _dealer_score -= 10
            ace_flag -= 1
    return  _player_score ,_dealer_score       



choiz = input("Do you want to play a game of Blackjack? Type 'y' or 'n':")
if choiz == "y":
  for i in range(2):
    player_cards.append(deal_card())
    dealer_cards.append(deal_card())
  print(f"player card: {player_cards}")   
  print(f"dealer cards: {dealer_cards}")  
  print(check_score(player_cards,dealer_cards))