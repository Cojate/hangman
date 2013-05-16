# Tell player 2 to look away

# Ask player 1 for a word

# Ask for a letter

# If letter matches any letter in the string

# If no, You draw hangman with new part

# If yes, print word with values in spot

# Checks is player 2 as won

# Add option to to guess word 

import string
from os import system


# global variable to keep track of misses
#misses = 0

""" 
#punc = []
#for symbol in string.punctuation:
#	punc.append(symbol)


# To be implemented later 

def punc_check(phrase)
test = False
while test == False:
	word = raw_input(prompt)
	for letter in word:
		if letter in punc:
			print "No symbols please."
		else:
			test = True
"""

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


#"""
#def misses():
#	global misses
#	misses = misses + 1
#
#	if misses == 1:
#		print """
#Head
#		"""
#	if misses == 2:
#		print """
#Body
#		"""
#
#	if misses == 3:
#		print """
#arms
#		"""
#"""



def guess():
	
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

	check_array = guess_array

	for i in range(len(word_array)):
		if guess == word_array[i]:
			guess_array[i] = guess

	#if guess_array == check_array:
	#	misses()

	print "".join(guess_array)



if __name__=="__main__":

	system('clear')
	
	print "Welcome to Hangman"
	print "One of you shoud look away"
	print "What is the phrase to be guessd??"
	
	word = raw_input("> ")
	system('clear')
	
	word_array = prepare(word)
	guess_array = blanks(word_array)
	
	while "-" in guess_array:
		guess()
		system('clear')














