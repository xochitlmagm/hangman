# this will be a simple hangman game where i learn python
#what will we need?
from random import random
#random, variables, boolean, input and output, integer, char, string, length, print

print("Hello! Welcome to the game of Hangman.")
print("Here are the rules:")
print("\tGuess the letters from a to b")
print("\tIf you get it wrong, the man loses a body part,")
print("\tIf you get it right, you are told and so far what you have is printed.")
print("\nAnd it continues")


# arrays for the different words and phrases:
words = ["hello", "mexico", "painting", "undocumented", "illiterate"]
phrases = ["why did the chicken cross the road", "I almost dropped my croissant", "well hello there"]

print(" ")
print(" ")

input("Are you ready? Press enter to start.")

print(" ")

choice = input("would you like to choose from 'words' or 'phrases'?")
#and the guessing starts
guess = input("your guess: ")


def choice_of_section():
    if choice == 'words':
        #something happens here
    elif choice == 'phrases':
        #and another goes Here
    else:
        print("hm, that does not seem right, please try again.")
