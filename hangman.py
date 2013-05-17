import string
from os import system

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

