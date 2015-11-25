# http://inventwithpython.com/chapter11.html

"""
Bagels is a deduction game you can play with a friend. Your friend thnks up a
random 3-digit number with no repeating digits, and you try to guess what that
number is. After each guess, your friend gives you three types of clues:

* Bagels - None of the three digits you guessed is the secret number.
* Pico - One of the digits is the secret number, but your guess has the digit in the wrong place.
* Fermi - Your guess has a correct digit in the correct place.

You can get multiple clues after each guess. If the secret number is ``456`` and
your guess is ``546``, the clues would be ``fermi pico pico``. The 6 provides
``fermi`` and the 5 and 4 provide ``pico pico``.
"""

import random


def getSecretNumber(numDigits):
    # Return a string that is numDigits long, made up of unique random digits.
    numbers = list(range(10))
    random.shuffle(numbers)
    secretNum = ''
    for i in range(numDigits):
        secretNum += str(numbers[i])
    return secretNum


def getClues(guess, secretNum):
    if guess == secretNum:
        print("You got it!")

    clue = []

    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            clue.append('Fermi')
        elif guess[i] in secretNum:
            clue.append('Pico')
    if len(clue) == 0:
        return 'Bagels'

    clue.sort()
    return ' '.join(clue)


def isOnlyDigits(num):
    if num == '':
        return False

    for i in num:
        if i not in '0 1 2 3 4 5 6 7 8 9'.split():
            return False

    return True


def playAgain():
    print("Do you want to play again? (yes or no)")
    return raw_input().lower().startswith('y')

NUMDIGITS = 3
MAXGUESS = 10

print("I am thinking of %s-digit number. Try to guess what it is." % (NUMDIGITS))
print("Here are some clues")
print('When I say:    That means:')
print('  Pico         One digit is correct but in the wrong position.')
print('  Fermi        One digit is correct and in the right position.')
print('  Bagels       No digit is correct.')

while True:
    secretNum = getSecretNumber(NUMDIGITS)
    print("I have thought up a number. You have %s guesses to get it." % (MAXGUESS))

    numGuesses = 1
    while numGuesses <= MAXGUESS:
        guess = ''
        while len(guess) != NUMDIGITS or not isOnlyDigits(guess):
            print("Guess #%s" % numGuesses)
            guess = raw_input()

        clue = getClues(guess, secretNum)
        print("Clue: %s" % clue)
        numGuesses += 1

        if guess == secretNum:
            break
        if numGuesses > MAXGUESS:
            print("You ran out of guesses. The answer was %s" % secretNum)

    if not playAgain():
        break
