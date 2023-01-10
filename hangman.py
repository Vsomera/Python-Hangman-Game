# ACIT 2515 - Hangman
# Vilmor Somera
# 01/09/23


""""
ACIT2515 Lab

Week 2 -- complete this file!

"""
import random

# The number of turns allowed is a global constant
NB_TURNS = 10

def pick_random_word():
    """
        Opens the words.txt file, picks and returns a random word from the file
    """
    # WRITE YOUR CODE HERE !
    with open("words.txt", "r") as file:
        return random.choice(file.readlines()).strip()

def show_letters_in_word(word, letters): 
    """
        This function RETURNS A STRING.
        This function scans the word letter by letter.
        First, make sure word is uppercase, and all letters are uppercase.
        If the letter of the word is in the list of letters, keep it.
        Otherwise, replace it with an underscore (_).

        DO NOT USE PRINT!

        Example:
        >>> show_letters_in_word("VANCOUVER", ["A", "V"])   
        'V A _ _ _ _ V _ _'
        >>> show_letters_in_word("TIM", ["G", "V"])
        '_ _ _'
        >>> show_letters_in_word("PIZZA", ["A", "I", "P", "Z"])
        'P I Z Z A'
    """
    # WRITE YOUR CODE HERE
    # my_string = ' '.join([x if x in letters else '_' for x in word])
    char_list = []

    for char in word:
        if char in letters:
            char_list.append(char)
        else:
            char_list.append('_')
    return ' '.join(char_list)


def all_letters_found(word, letters):
    """
        Returns True if all letters in word are in the list 'letters'
    """
    return '_' not in show_letters_in_word(word, letters)
        

def main(turns):
    """
        Runs the game. Allows for "turns" loops (attempts).
        At each turn:
        1. Ask the user for a letter
        2. Add the letter to the list of letters already tried by the player
        3. If the letter was already tried, ask again
        4. Use the show_letters_in_word function to display hints about the word
        5. Remove 1 to the number of tries left
        6. Check if the player
            - won (= word has been found)
            - lost (= word has not been found, no tries left)

        Do not forget to pick a random word first :-)
    """

    word = pick_random_word()
    letters = []

    while not all_letters_found(word, letters) and turns > 0:
        print(f'Word: {show_letters_in_word(word, letters)}')
        print(f'Tries remaining: {turns}')
        letter = input('Enter a letter: ')
        if letter in letters:
            print('You have already tried this letter.')
        else:
            letters.append(letter)
            if letter in word:
                print('This letter is in the word!')
            else:
                print('This letter is not in the word.')
                turns -= 1
    
    if all_letters_found(word, letters):
        print(f'Congratulations! You found the word {word}.')
    else:
        print(f'You have no more tries left. The word was {word}.')


if __name__ == "__main__":
    main(NB_TURNS)


