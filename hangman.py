# COMP 1516 - OOP
# Vilmor Somera
# 01/16/22

import pytest
import random


class SecretWord:
    def __init__(self, word=None):
        self.secret_word = word
        if word is None:
            with open('words.txt', 'r') as f:
                words = f.read().splitlines()
                self.secret_word = random.choice(words)
    
    def show_letters(self, letters):
        word = ''
        for char in self.secret_word:
            if char in letters:
                word += char
            else:
                word += '_'
        return word
    
    def check_letters(self, letters):
        for char in self.secret_word:
            if char not in letters:
                return False
        return True
    
    def check(self, word):
        return word.lower() == self.secret_word.lower()

class Game:
    def __init__(self, turns=10):
        self.secret_word = SecretWord()
        self.turns = turns
        self.tried_letters = []
    
    def play_one_round(self):
        letter_or_word = input("Enter a letter or a word: ").lower()
        if letter_or_word in self.tried_letters:
            print("You already tried that letter.")
            return self.play_one_round()
        
        self.tried_letters.append(letter_or_word)
        print(self.secret_word.show_letters(self.tried_letters))
        self.turns -= 1
        
        if len(letter_or_word) > 1:
            if self.secret_word.check(letter_or_word):
                return True
        else:
            if self.secret_word.check_letters(self.tried_letters):
                return True
        return False
    
    def play(self):
        while self.turns > 0:
            if self.play_one_round():
                print("You won!")
                return True
            if self.turns == 0:
                print(f"You lost!")
                return False
        return False

