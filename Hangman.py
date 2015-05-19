import time #Can sleep 
import random

WORDS = 'ant baboon yahoo urinary umbrella ignition winter'.split()

def randomizeWordToGuess(wordList):
	#This function chooses a word for the player to guess
	wordIndex = random.randint(0, len(wordList) - 1)
	return wordList[wordIndex]

def displayBoard(missedLetters, correctLetters, wordToGuess):
	#Shows the word and what letters you've guessed
	print("Missed Letters: ", end= '')
	for letter in missedLetters:
		print(letter, end='')
	print("\n")
	
	blanks = '_' * len(wordToGuess)
	
	for i in range(len(wordToGuess)):
		if(wordToGuess[i] in correctLetters):
			blanks = blanks[:i] + wordToGuess[i] + blanks[i+1:]
	
	for letter in blanks:
		print (letter, end=' ')
	print("\n")
	
def getGuess(guesses, wordToGuess):
	#Returns the letter the player entered. Makes sure they type in one character
	while True:
		print("Guess a letter.")
		guess = input()
		guess = guess.lower()
		if guess == "cheat":
			print("Cheater!! The word is ", wordToGuess)
		elif len(guess) != 1:
			print('Please enter a single letter.')
		elif guess in guesses:
			print("You've already guessed that letter. Choose again")
		elif guess not in 'abcdefghijklmnopqrstuvwxyz':
			print("Please enter a LETTER.")
		
		else:
			return guess

			
def replay():
	char = input("Do you want to play again? (Type y or n) ")
	if char == 'y':
		return True


name = input("What is your name? ")

print ("Hello, " + name, "! Time to play some Hangman!", "\n")

#wait for 1 second
time.sleep(1)

print ("Start guessing...")
time.sleep(0.5)

#here we set the word to guess
missedLetters = ''
correctLetters = ''
wordToGuess = randomizeWordToGuess(WORDS)
gameIsDone = False

#determine # of turns
turns = 7

#check if turns are up
while(turns > 0): 
	displayBoard(missedLetters, correctLetters, wordToGuess)
	guess = getGuess(missedLetters + correctLetters, wordToGuess)
	if guess in wordToGuess:
		correctLetters += guess
		#Checks if player won
		foundAllLetters = True
		for i in range(len(wordToGuess)):
			if wordToGuess[i] not in correctLetters:
				foundAllLetters = False
				break
		
		if foundAllLetters:
			print("Congrats. You won")
			gameIsDone = True
	else:
		missedLetters += guess
		turns -= 1
		if turns == 0:
			displayBoard(missedLetters, correctLetters, wordToGuess)
			print("You lost. The secret word is ", wordToGuess)
			gameIsDone = True
		
	if gameIsDone:
			if replay():
				missedLetters = ''
				correctLetters = ''
				wordToGuess = randomizeWordToGuess(WORDS)
				gameIsDone = False
			else:
				print("Thanks for playing!")
				break