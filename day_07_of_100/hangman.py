from random import choice 
import re
from hangman_arts import *

is_running  = True

list_of_words =["abruptly","absurd","abyss","affix","askew","avenue","awkward","axiom","azure","bagpipes","bandwagon","banjo","bayou","beekeeper","bikini","blitz","blizzard","boggle","bookworm","boxcar","boxful","buckaroo","buffalo","buffoon","buxom","buzzard","buzzing","buzzwords","caliph","cobweb","cockiness","croquet","crypt","curacao","cycle","daiquiri","dirndl","disavow","dizzying","duplex","dwarves","embezzle","equip","espionage","euouae","exodus","faking","fishhook","fixable","fjord","flapjack","flopping","fluffiness","flyby","foxglove","frazzled","frizzled","fuchsia","funny","gabby","galaxy","galvanize","gazebo","giaour","gizmo","glowworm","glyph","gnarly","gnostic","gossip","grogginess","haiku","haphazard","hyphen","iatrogenic","icebox","injury","ivory","ivy","jackpot","jaundice","jawbreaker","jaywalk","jazziest","jazzy","jelly","jigsaw","jinx","jiujitsu","jockey","jogging","joking","jovial","joyful","juicy","jukebox","jumbo","kayak","kazoo","keyhole","khaki","kilobyte","kiosk","kitsch","kiwifruit","klutz","knapsack","larynx","lengths","lucky","luxury","lymph","marquis","matrix","megahertz","microwave","mnemonic","mystify","naphtha","nightclub","nowadays","numbskull","nymph","onyx","ovary","oxidize","oxygen","pajama","peekaboo","phlegm","pixel","pizazz","pneumonia","polka","pshaw","psyche","puppy","puzzling","quartz","queue","quips","quixotic","quiz","quizzes","quorum","razzmatazz","rhubarb","rhythm","rickshaw","schnapps","scratch","shiv","snazzy","sphinx","spritz","squawk","staff","strength","strengths","stretch","stronghold","stymied","subway","swivel","syndrome","thriftless","thumbscrew","topaz","transcript","transgress","transplant","triphthong","twelfth","twelfths","unknown","unworthy","unzip","uptown","vaporize","vixen","vodka","voodoo","vortex","voyeurism","walkway","waltz","wave","wavy","waxy","wellspring","wheezy","whiskey","whizzing","whomever","wimpy","witchcraft","wizard","woozy","wristwatch","wyvern","xylophone","yachtsman","yippee","yoked","youthful","yummy","zephyr","zigzag","zigzagging","zilch","zipper","zodiac","zombie"]
fail  = 0
target_word = choice(list_of_words).upper()
word_count = 0
occurences = []
current_progress = ""
current_progress_list = []
found_letters =[]
repeat_entry = False

for letter in target_word:
    current_progress_list.append("_")
    current_progress += "_"


while is_running:
    print(current_progress)
    letter = input("Guess a letter:").upper()

    for index in re.finditer(letter,target_word):
        try:
            occurences.append(index.start())
            for indexes in occurences:
                current_progress_list[indexes] = letter
        except IndexError:
            pass
    if letter not in found_letters:
        found_letters += letter    
        if len(occurences) > 0:       
            word_count += len(occurences)  
        else:
             fail += 1     
    elif len(occurences) ==0 :
        fail += 1      

    current_progress = ""
    for letters in current_progress_list :
        current_progress += letters
    if fail < len(HANGMANPICS)-1:       
        print(HANGMANPICS[fail])
    else:
        is_running = False
        print("GAME OVER")
    
    if current_progress == target_word:
        is_running = False
        print("YOU WIN")
    occurences = []
