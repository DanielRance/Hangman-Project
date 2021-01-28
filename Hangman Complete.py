# -*- coding: utf-8 -*-
"""
Created on Thu Jan 28 03:36:57 2021

@author: Daniel Rance
"""

# Player1Word = input("Player 1, please enter the word you would like Player 2 to guess: ")
# print(chr(27) + "[2J") 
import random
from words import word_list

def get_word():
    word = random.choice(word_list)
    return word.upper() #returns in all upper case

def play(word):
    wordCompletion = "_" * len(word)
    correctGuess = False
    guessedLetters = []
    guessedWords = []
    lives = 6
    print("Let's play Hangman!")
    print(displayHangman(lives))
    print(wordCompletion)
    print("\n")
    while not correctGuess and lives > 0:
        userGuess = input("Please enter a letter or word: ").upper()
        if len(userGuess) == 1 and userGuess.isalpha(): #if the user has entered a single letter, isalpha() checks if something is a letter
            if userGuess in guessedLetters:
                print("You have already guessed this letter, please try again.")
            elif userGuess not in word:
                print(userGuess, " is not in the word.")
                lives -= 1
                print("You have ", lives, " lives left.")
                guessedLetters.append(userGuess)
            else:
                print("Good job!", userGuess, "is in the word.")
                guessedLetters.append(userGuess)
                wordAsList = list(wordCompletion)
                indices = [i for i, letter in enumerate(word) if letter == userGuess]
                for index in indices:
                    wordAsList[index] = userGuess
                wordCompletion = "".join(wordAsList) #converts the list of letters back into one string
                if "_" not in wordCompletion: #if the word has been fully guessed
                    correctGuess = True
        elif len(userGuess) == len(word) and userGuess.isalpha():
            if userGuess in guessedWords:
                print("You have already guessed this word.")
            elif userGuess != word:
                print(userGuess, "is not the word. Please try again.")
                lives -= 1
                guessedWords.append(userGuess)
            else:
                correctGuess = True
                wordCompletion = word
        else:
            print("Not a valid guess, please try again.")
        print(displayHangman(lives))
        print(wordCompletion)
        print("\n")
    if correctGuess: #if correctGuess is true
        print("Congrats on guessing the correct word, you win!")
    else:
        print("Sorry, you ran out of tries. The word was " + word + ". Please try again.")
        
def displayHangman(tries):
    stages = [  # final state: head, torso, both arms, and both legs
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # head, torso, both arms, and one leg
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                # head, torso, and both arms
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                # head, torso, and one arm
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                # head and torso
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                # head
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                # initial empty state
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return stages[tries]        
    
def main():
    word = get_word()
    play(word)
    while input("Play again? (Y/N)").upper() == "Y":
        word = get_word()
        play(word)

if __name__ == "__main__":
    main()
    
        