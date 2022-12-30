import random
from art import *
from game_data import data

score = 0
selection_b = None


def choose(_previous_index):
    while True:
        selected_index = random.randint(0, len(data) - 1)
        if selected_index != _previous_index:
            chosen = data[selected_index]
            _previous_index = selected_index
            return chosen, _previous_index


def play():
    global selection_a
    global score
    game_over = False
    selection_b, index_b = choose(random.randint(0, len(data) - 1))
    print(
        f'Compare A: {selection_a["name"]},{selection_a["description"]} from {selection_a["country"]}'
    )
    print(vs)
    print(
        f'Against B: {selection_b["name"]},{selection_b["description"]} from {selection_b["country"]}'
    )
    choice = input("Who has more Instagram Followers? Type 'A' or 'B': ").lower()
    if choice == "a":
        if selection_a['follower_count'] >= selection_b['follower_count']:
          score += 1
          print("Correct")
        else:
          game_over = True
          print(f"inorrect you scored {score} points")
    elif choice == "b":
        if selection_b['follower_count'] >= selection_a['follower_count']:
          score += 1
          print("Correct")
        else:
          game_over = True      
          print(f"inorrect you scores {score} points")
  
    selection_a = selection_b  
    if not game_over:
      play()


selection_a, index_a = choose(random.randint(0, len(data) - 1))
print(logo)
play()
