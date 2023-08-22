import json
import random
import unicodedata


class Player:

    def __init__(self):
        self.score = 0

    # setter for score
    def set_score(self, score):
        self.score += score

    def get_score(self):
        return self.score

    def set_word(self, word):
        self.word = word

    def get_word(self):
        return self.word


class Computer(Player):
    def __init__(self):
        self.word = []
        self.letters = []

    def set_word(self, word):
        self.word = word

    def get_word(self):
        return self.word

    def set_letters(self, letters):
        self.letters = letters

    def get_letters(self):
        return self.letters

    def smart(self, words, given_letters):
        possible_words = []
        for i in words:
            for word in i:
                letter_count = {}
                for letter in word:
                    letter_count[letter] = letter_count.get(letter, 0) + 1

                can_form_word = True
                for letter, count in letter_count.items():
                    if given_letters.count(letter) < count:
                        can_form_word = False
                        break

                if can_form_word:
                    possible_words.append(word)

        return possible_words


class Human(Player):

    def __init__(self):
        super().__init__()
        self.name = None
        self.word = None
        self.letters = []

    # setter for the human name
    def set_name(self):
        self.name = self.give_name()

    def set_word(self):
        super().set_word(self.give_word().upper())

    def set_letters(self, letters):
        self.letters = letters

    def get_letters(self):
        return self.letters

    def get_name(self):
        return self.name

    def get_word(self):
        return super().get_word()

    # input the possible word for the game
    def give_word(self):
        return input("Εισάγετε την επιθυμητή λέξη:")

    # input the name
    def give_name(self):
        return input("Εισάγετε όνομα παίχτη:")


class SakClass:

    # constructor with no arguments passed
    def __init__(self):
        self.words = {}
        self.letters = {}
        self.sak = []
        self.final_letters = []
        self.create_words()
        self.create_letters()
        self.create_sak()

    # creates the words that contains all the words for file greek7.txt
    def create_words(self):
        with open("greek7.txt", "r", encoding="utf-8") as file:
            lines = file.readlines()

            for word in lines:
                self.words.setdefault(word[0], []).append(word.strip())

    # creates the dictionary letters which has the number of letters and their points
    def create_letters(self):
        # self.letters = {'Α': [0, 1], 'Β': [0, 8], 'Γ': [0, 4], 'Δ': [2, 4], 'Ε': [8, 1],
        #                 'Ζ': [0, 10], 'Η': [0, 1], 'Θ': [0, 10], 'Ι': [8, 1], 'Κ': [4, 2],
        #                 'Λ': [0, 3], 'Μ': [0, 3], 'Ν': [0, 1], 'Ξ': [1, 10], 'Ο': [9, 1],
        #                 'Π': [0, 2], 'Ρ': [0, 2], 'Σ': [0, 1], 'Τ': [0, 1], 'Υ': [4, 2],
        #                 'Φ': [0, 8], 'Χ': [0, 8], 'Ψ': [0, 10], 'Ω': [0, 3]
        #                 }
        self.letters = {'Α': [12, 1], 'Β': [1, 8], 'Γ': [2, 4], 'Δ': [2, 4], 'Ε': [8, 1],
                        'Ζ': [1, 10], 'Η': [7, 1], 'Θ': [1, 10], 'Ι': [8, 1], 'Κ': [4, 2],
                        'Λ': [3, 3], 'Μ': [3, 3], 'Ν': [6, 1], 'Ξ': [1, 10], 'Ο': [9, 1],
                        'Π': [4, 2], 'Ρ': [5, 2], 'Σ': [7, 1], 'Τ': [8, 1], 'Υ': [4, 2],
                        'Φ': [1, 8], 'Χ': [1, 8], 'Ψ': [1, 10], 'Ω': [3, 3]
                        }

    # creates the sak list
    def create_sak(self):
        for i in self.letters:
            for j in range(self.letters.get(i)[0]):
                self.sak.append(i)

    # getter for final_letters
    def get_final_letters(self):
        return self.final_letters

    # getter for letters
    def get_letters(self):
        return self.letters

    def get_words(self):
        words = []
        for i in self.words:
            words.append(self.words.get(i))
        return words

    # prints the remaining letters
    def print_letters(self):
        for i in self.letters:
            print(i + "," + str(self.letters.get(i)[0]))

    def get_letters_7(self):
        return self.letters_7

    # reduces the amount of a letters in the letters dictionary
    def reduce_letter_count(self, key):
        self.letters[key][0] -= 1

        # gives 7 random numbers from the sak list and decreases from the letter dictionary

    def give_letters(self, letters):
        if len(self.sak) < 7:
            print("Το παιχνίδι τελείωσε.Δεν υπάρχουν άλλα διαθέσιμα γράμματα.")
        else:
            random.shuffle(self.sak)
            letters += random.sample(self.sak, 7 - len(letters))
            for i in self.final_letters:
                # print(str(self.letters.get(i)[0]) + " me")
                self.reduce_letter_count(i)

            return letters

    # checks if the given word is greek or not
    def is_greek(self, word):
        for i in word:
            if 'GREEK' in unicodedata.name(i, ''):
                return True

        return False

    # checks if the word letters concluded in the given letters
    def check_letters(self, tmp1, letters):
        word = list(tmp1)
        count = 0
        j = 0
        for i in range(len(word)):
            for j in range(len(letters)):
                if (word[i] == letters[j]):
                    count += 1
                    letters.remove(letters[j])
                    break

        if count == len(word):
            return True
        return False

    # finds if the word is in the words dictionary
    def word_search(self, word):

        if word in self.words[word[0]]:
            print("Η λέξη είναι αποδεκτή!")
            return True
        else:
            print("Η λέξη " + str(word) + " δεν είναι αποδεκτή!")
            return False

    # calculates the total points of the given word
    def count_points(self, word):

        tmp = word.upper()
        word = tmp
        points = 0
        for i in word:
            points += self.letters.get(i)[1]
        return points

    def find_max_points(self, words):
        max_word = None
        max = 0
        for i in words:
            tmp = self.count_points(i)
            if tmp > max:
                max = tmp
                max_word = i
        return max_word, max

    def find_max_2_points(self, words):
        max1_word = None
        max1 = 0
        max2_word = None
        max2 = -1
        for i in words:
            tmp = self.count_points(i)
            if tmp > max1:
                max2 = max1
                max2_word = max1_word
                max1 = tmp
                max1_word = i
            else:
                if max1 > tmp > max2:
                    max2 = tmp
                    max2_word = i

        return max1_word, max2_word


# while not a.is_greek(f):
#     f = input("Enter word")
# if a.check_letters(temp, f):
#     a.word_search(f)
# else:
#     print("The letters are not correct ")


class Statistics:
    def __init__(self):
        self.stats = {}

        self.stats = self.get_file_statistics()

    def get_file_statistics(self):
        with open('statistics', 'r') as f:
            return json.load(f)

    def unique_username(self, name):
        if name in self.stats:
            print("Το όνομα παίχτη υπάρχει ήδη.")
            return False
        else:
            return True

    def add_element(self, name, score):
        self.stats[name] = score
        with open('statistics', 'w') as f:
            json.dump(self.stats, f)

    def print_stats(self):
        sorted_stats = sorted(self.stats.items(), key=lambda x: x[1], reverse=True)
        print("Τα σκορ των παιχτών από το μεγαλύτερο στο μικρότερο:")
        for item in sorted_stats:
            print(str(item[0]) + ": " + str(item[1]))
        print("")
