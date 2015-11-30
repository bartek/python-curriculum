Bagels
======

Bagels is a deduction game you can play with a friend. Your friend thinks up a
random 3-digit number with no repeating digits, and you try to guess what that
number is. After each guess, your friend gives you three types of clues:

* Bagels - None of the three digits you guessed is the secret number.
* Pico - One of the digits is the secret number, but your guess has the digit in the wrong place.
* Fermi - Your guess has a correct digit in the correct place.

You can get multiple clues after each guess. If the secret number is ``456`` and
your guess is ``546``, the clues would be ``fermi pico pico``. The 6 provides
``fermi`` and the 5 and 4 provide ``pico pico``.

Below you'll find the pieces of this program. Your mission is to fill in the
missing pieces (All denoted by ``____________`` lines), and get the Bagel game
working.

Think about how you worked on your trivia and hang man games. They are very
similar in style and functionality compared to this.

Breaking down the program
-------------------------

Many times, a great way to understand how to build a complex program is by
breaking it down into smaller bits. It's hard to tell someone how Bagels works
and then expect them to explain how to build it, but if you think about the
smaller pieces, it becomes a little easier.

Let's think about Bagels and see if we can identify the parts of the program.

* First, re-reading the game notes, we see that a "friend thinks of a 3-digit
  number". In this case, that friend will be the computer. So, perhaps we will
  need **a function that can generate a random 3 digit number**
* We can see that we will need to be able to guess the number, so we will need
  **a function that allows for user input**
* Then, we will get clues about our guess. We will need **a function or code
  that checks the players input (guess) and provides the clues**
* Finally, because this is a game, we will need to have a game loop. This has
  actually been provided for you in the exercise below.

Overall, the games style is very similar to the Trivia/Hangman games we worked
on, but it'll be best if we take it step by step. So let's do that.

Generating a secret number
--------------------------

The first step is having the computer generate a random 3 digit number. We did a
little bit of this previously. Let's look at what that function may look like:


.. sourcecode:: python

   def getSecretNumber():
      # Remember, anything that has the # before it is a comment. Python ignores
      # these and they are purely for your reference.

      # Collect a bunch of random numbers from 0-9 to be used in our final
      # secret number.
      numbers = list(range(10))
      random.shuffle(numbers)
      secretNumber = ''

      # How do we loop again? Here I use range to loop 3 times, because our
      # secret number is 3 digits long. Fill in the blanks.
      ____________ in range(3):
         # For each loop iteration, we want to get a number from `numbers`. Do
         # you remember how to access items in a list? Ask your mentor/teacher
         # if you're not sure!
         secretNumber += str(_______________)

      return secretNumber

That's great. Once this function is complete you can run it by calling it, like
so:

.. sourcecode:: python

   print(getSecretNumber())

Each time you will see a different number. If not, look over your code.

**Bonus**: How can you change the ``getSecretNumber`` function so that it will
take **one parameter** that lets the user change the amount of digits in the
secret number. Once the parameter is passed, where else in the function would
you have to change code?

Figuring out what clues to display
-----------------------------------

Next, let's build a function that takes the a ``guess``, and the
``secretNumber`` and returns the clues for us. Remember to read at the start of
this exercise what clues should show up when.

Let's look at the function with some pieces missing. You must fill in the
missing bits.

.. sourcecode:: python

  def getClues(guess, secretNumber):
    # When is the user guess going to be correct? What values must we compare
    # for the winning condition?
    if ________________:
      print("You got it!")

    clue = []

    # Let's check each number in the guess and see what clue to give.
    for i in range(len(guess)):
      # This number is in the correct spot within the secret number. What clue
      # do we give them?
      if guess[i] == secretNumber[i]:
        clue.append('_________________')
      # The clue is in the secretNumber but not in the right spot. What variable
      # must we check and what clue do we give?
      elif guess[i] in ____________:
        clue.append('____________')

    # If no clues were added, what must we return to the user?
    if len(clue) == 0:
      ___________________

    clue.sort()
    return ' '.join(clue)


Remember you can test the function by calling ``getClues()`` with the two
parameters it expects.

Building the game loop
----------------------

Now it's time to build the game loop and piece your functions together. First,
we will create these two functions. They have been completed for you, just need
to type them out.

.. sourcecode:: python

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


Now, the final game loop. Again, there are pieces missing signified by `____________`. A lot of this is customizable to your desires, simply adjust the wording as you wish.

.. sourcecode:: python

  # We must set the number of digits the secret number is. 3 is pretty hard, but
  # you can always give your friends a harder number.
  NUMDIGITS = 3

  # How many guesses does the player get?
  MAXGUESS = 10

  print("I am thinking of %s-digit number. Try to guess what it is." % (NUMDIGITS))
  print("Here are some clues")
  print('When I say:    That means:')
  print('  Pico         One digit is correct but in the wrong position.')
  print('  Fermi        One digit is correct and in the right position.')
  print('  Bagels       No digit is correct.')

  # How do we run a loop forever?
  while ____________:

      # What function must we call to get our secret number?
      secretNum = _________________

      # Fill in the blanks!
      print("I have thought up a number. You have %s guesses to get it." % (__________))

      numGuesses = 1
      # What variable are we using to track the amount of current guesses? Hint: It's nearby!
      while __________ <= MAXGUESS:
          guess = ''
          while len(guess) != NUMDIGITS or not isOnlyDigits(guess):
              print("Guess #%s" % numGuesses)
              # How do we ask for input from the user?
              guess = ______________

          # What function did we build to get clues? Make sure you pass all the
          # expected parameters.
          clue = ___________________-
          print("Clue: %s" % clue)

          # What must we do to make sure that the number of guesses is going up,
          # so they can't guess forever? Obviously we must do something with this
          # numGuesses variable!
          numGuesses ________________

          # What condition would decide to break out of the game loop and end the game?
          if ____________:
              break

          # IF they ran out of guesses, we let them know.
          if numGuesses > MAXGUESS:
              print("You ran out of guesses. The answer was %s" % secretNum)

      if not playAgain():
          break


Once you've filled in the blanks, it's time to try your program out and debug.
You might find problems but don't worry, you can fix them, just keep playing
with the program and you'll figure it out!
