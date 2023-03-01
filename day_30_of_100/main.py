import pandas as pd

df = pd.read_csv("day_26_of_100/nato_phonetic_alphabet.csv")
# print (df)


#  using iterrows to loop through the dataframe 
data_dict = {row.letter:row.code for(index,row) in df.iterrows()}


def get_word():
    word = input("Type the word you want to spell using the nato alphabet: ").upper()
    try: 
        alpa_list = [data_dict[key] for key in word]
        

    except KeyError:
        print("Sorry only letters are allowed")
        get_word()
    else:
        print(alpa_list)

get_word()


