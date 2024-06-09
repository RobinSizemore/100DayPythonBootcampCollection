# Comprehension Understanding Exercise
import pandas

nato_df = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {row.letter: row.code for (index, row) in nato_df.iterrows()}  # pandas df to dictionary using comprehension
entered_word = ""
while not entered_word == 'QUIT':
    entered_word = input("Please enter the word to transcribe: ").upper()
    try:
        list_output = [nato_dict[letter] for letter in entered_word]  # word to list using dict and comprehension
        print(list_output)
    except KeyError as error_msg:
        print(f"Please enter only letters in the alphabet. {error_msg} is unacceptable.")
