from random import choice 

player_cards = []
dealer_cards = []
player_stake = 0
player_cash  = 1000
player_score = 0
dealer_score = 0
cashout =False
is_running = True
def deal_card():
  """ returns a random card from the deck"""
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  return choice(cards)
def check_cards(_player_cards,_dealer_cards):
    """takes player's cards and dealer's cards as input and computes the scores. it returns in order of it's arguements"""
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

def show_stat():
        """displays player score and cash """
        a,b = check_cards(player_cards,dealer_cards)
        print(f"player card: {player_cards}")   
        print(f"player score: {a} player cash : {player_cash}")   
        print(f"dealer cards:[*, {dealer_cards[1]}]") 

def check_score(_player_score,_dealer_score):
    pass  

option = input("Do you want to play a game of Blackjack? Type 'y' or 'n':")
if option == "y":
  for i in range(2):
    player_cards.append(deal_card())
    dealer_cards.append(deal_card())
  show_stat()
while is_running:
    if input("hit or stand? Type 'h' or 's': ") == 'h':
        player_cards.append(deal_card())
        show_stat()                    

    else:
         a,b = check_cards(player_cards,dealer_cards) 
         while b < 17:
            dealer_cards.append(deal_card())
            a,b = check_cards(player_cards,dealer_cards) 
         print(a,b)  
