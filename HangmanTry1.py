from itertools import repeat # for checking whether a word has more then one of the same type characters
import random  # imports the random function to choose a random word from the word list

print("===================================")
print("Start of code")

def choose_letter():
    for letter in secretWord:  # for each letter in secretWord
        if (letter in correctGuessedCharacter):
            print(letter, end="")  # prints the correctGuessedCharacter word
        else:
            print('#', end="")  # prints underscores in the place of the unguessed word


tries = 9 #tries


with open('usa.txt', 'r') as f:
    words = f.readlines()
  # makes the usa.txt file readable

# chooses a random word from the usa file
secretWord = random.choice(words).upper().strip()


# creates two lists, one for the correct guessed characters and one for the opposite
incorrectGuessedCharacter = []
correctGuessedCharacter = []

print('You have 10 tries only!') #prints out how many tries you have

# check whether the tries are over 0
while True:

    # displays each unguessed character as a _ or as the correctGuessedCharacter character
    choose_letter()

    print("\n===================================")
    guess = input("\nEnter a guess: ").upper()


    if guess.isalpha() == False:
        print("===================================")
        print('Please enter a character only!')            # checks if its only english characters
        print("===================================")
    
    elif len(guess) > 1:
        print("===================================")
        print('Please only enter one character only!')   # checks if the guess has more then 1 letter
        print("===================================")

    elif guess in correctGuessedCharacter:      # if the guessedCharacter letter is already chosen before
        print("===================================")
        print('Character already chosen! Choose a new one') 
        
        print("===================================")
    
    elif guess in incorrectGuessedCharacter:      # if the guessedCharacter letter is already chosen before
        print("===================================")
        print('Character already chosen! Choose a new one') 
        tries -= 1
        print(str(tries) + ' tries left')
        print("===================================")

    # if the guessedCharacter letter is not already in but is correct
    elif guess in secretWord:
        print("===================================")
        print('Correct! Character is in the word!')
        correctGuessedCharacter.extend(repeat(guess, secretWord.count(guess)))  
        print("===================================")

    # if the guess is wrong, removes a try and adds the guess in the incorrectGuessCharacter
    else:
        print("===================================")
        print('Wrong guess!\nYou have ' + str(tries) + ' left!')
        incorrectGuessedCharacter.append(guess)
        tries -= 1
        print("===================================")

    # checks whether you have tries, if you don't, you lose
    if tries == 0:
        print('You have lost!')
        print('The word was: ' + secretWord)
        print("===================================")
        break

    # checks if you have the same amount of correctlyGuessedCharacters as the secretWords character
    if len(correctGuessedCharacter) == len(secretWord):
        print('You won the game! Congrats!')
        print('')
        print('\nThe secret word was: ' + secretWord)
        print("===================================")
        break


print("End of code")
print("===================================")