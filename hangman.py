# Add option to to guess word 

import string
from os import system
from art import *
from time import sleep


# global variable to keep track of misses
misses = 0


def prepare(phrase):
	array = []
	phrase_array = phrase.split()
	edited_phrase = " ".join(phrase_array).upper()
	for i in edited_phrase:
		array.append(i)
	return array

def blanks(letters):
	guess_array = []
	for letter in letters:
		if letter == " ":
			guess_array.append(" ")
		else:
			guess_array.append("-")
	return guess_array


def guess():
	
	system('clear')
	hangman(misses)
	
	print "Misses: ", misses
	print ""
	print "".join(guess_array)
	print ""
	print "Guess a letter: "

	test = False
	while test == False:
		guess = raw_input("> ").upper()
		
		# checks if guess is only one letter
		if len(guess) == 1:
			test = True
		else:
			print "Only one letter please."
			print ""

	# creates array to check if guess is contained in word_array
	check_array = guess_array[:]

	for i in range(len(word_array)):
		if guess == word_array[i]:
			guess_array[i] = guess

	if guess_array == check_array:
		global misses
		misses += 1

if __name__=="__main__":

	system('clear')
	
	title()
	print "What is the phrase to be guessd??"
	
	word = raw_input("> ")
	system('clear')
	
	word_array = prepare(word)
	guess_array = blanks(word_array)
	
	while "-" in guess_array:
		guess()
		system('clear')
		if misses == 5:
			hangman(misses)
			break

	print "The phrase was: " , "".join(word_array)
	print ""
	print "Thanks for playing..."
	title()





