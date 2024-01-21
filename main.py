import pandas as pd

data = pd.read_csv("nato_phonetic_alphabet.csv")
print(data)


nato_alpha = {row.letter: row.code for (index, row) in data.iterrows()}
# print(nato_alpha)

text = input("enter a string to covert :").upper()

list_text = []
for i in text:
    list_text.append(i)

# print(list_text)

new_dict = {key: value for key, value in nato_alpha.items() if key in list_text}

print(new_dict)
