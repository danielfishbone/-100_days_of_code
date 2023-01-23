import pandas as pd

df = pd.read_csv("day_26_of_100/nato_phonetic_alphabet.csv")
word = input("Type the word you want to spell using the nato alphabet: ").capitalize()
print (df)

letter = df.letter
code = df.code



data_dict = {row.letter:row.code for(index,row) in df.iterrows()}

alpa_list = []



