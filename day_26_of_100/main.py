import pandas as pd

df = pd.read_csv("day_26_of_100/nato_phonetic_alphabet.csv")
word = input("Type the word you want to spell using the nato alphabet: ").upper()
# print (df)

letter = df.letter
code = df.code


#  using iterrows to loop through the dataframe 
data_dict = {row.letter:row.code for(index,row) in df.iterrows()}
# print(data_dict)


alpa_list = [data_dict[key] for key in word]

print(alpa_list)

