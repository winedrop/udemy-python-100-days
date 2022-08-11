# student_dict = {
#     "student": ["Angela", "James", "Lily"], 
#     "score": [56, 76, 98]
# }

# #Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#     pass

# import pandas
# student_data_frame = pandas.DataFrame(student_dict)

# #Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

import pandas as pd

#TODO 1. Create a dictionary in this format:
#{"A": "Alfa", "B": "Bravo"}

nato_phonetic_data = pd.read_csv("26_day_list_comprehension/nato_phonetic_alphabet.csv",index_col= "letter" )
#


#nato_phonetic_dict = {row.letter:row.code for (index, row) in nato_phonetic_data.iterrows()}
#print(nato_phonetic_dict)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

name_input = input("Enter your value: ")

# nato_spelling = [nato_phonetic_dict[letter.upper()] for letter in name_input if letter.upper() in nato_phonetic_dict]

nato_spelling = [nato_phonetic_data.loc[letter.upper(), "code"] for letter in name_input if letter.upper() in nato_phonetic_data.index]

print(nato_spelling)

