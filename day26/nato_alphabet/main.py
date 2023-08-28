# TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.

import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

# wrong:
# nato_dict = data.to_dict()
# {
#     'letter': {0: 'A', 1: 'B'}, 
#     'code': {0: 'Alfa', 1: 'Bravo'}
# }

# without list comprehension:
# nato_dict = {}
# for (index, row) in data.iterrows():
#     nato_dict[row.letter] = row.code

nato_dict = {row.letter:row.code for (index, row) in data.iterrows()}

word = input("Enter a word: ").upper()

# without list comprehension:
# result = []
# for i in word:
#     result.append(nato_dict[i])

result = [nato_dict[i] for i in word]

print(result)
