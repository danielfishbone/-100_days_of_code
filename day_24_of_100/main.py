#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

from cgitb import text


with open("/home/fishbone/python_100_days_of_code/day_24_of_100/Input/Names/invited_names.txt") as name_file:
    names = name_file.readlines()
with open("/home/fishbone/python_100_days_of_code/day_24_of_100/Input/Letters/starting_letter.txt") as letter_file:
    letter = letter_file.read()

stripped_names =[]
for name in names:
    stripped_names.append(name.strip())

  
for name in stripped_names:
    new_letter = letter.replace("[name]", name)
    with open(f"/home/fishbone/python_100_days_of_code/day_24_of_100/Output/ReadyToSend/letter_for_{name}.txt","w")as ready_letter:
        ready_letter.write(new_letter)


