import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")


def main():
    nato_dict = {row.letter: row.code for (index, row) in data.iterrows()}
    end_loop = True
    while end_loop:
        user_input = input("hii welcome to liron nato phonetic program enter the word you want to phonet:").upper()
        try:
            nato_words = [nato_dict[letter] for letter in user_input]
            print(nato_words)
            end_loop = False
        except KeyError:
            print("Sorry, only letters in the alphabet please")




if __name__ == "__main__":
    main()
