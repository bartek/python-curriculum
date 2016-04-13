Iteration, Reviewed (Lesson 7)
##############################

Now that we've had some time to understand all sorts of fundamentals of Python,
we need to focus on iteration. Iteration is important because it allows us to do
something more than once. That something is usually a task we want to repeat a
set number of times.

For example, what if a game has two or more players? We want to do the same
thing until all players have had a chance. This is what we call iteration, or
*looping*.

Setting It Up
-------------

Before we can learn about iteration in detail, let's build the basics of our
game. We'll do something we've done before,  which is a simple trivia game, but
we'll spruce it up with some new techniques that we'll learn today.

First, we're going to build a list of words. Remember, lists are like buckets
for variables, strings, and numbers. We can put whatever inside them, and we use
the square brackets to open and close the bucket. Let's do that first.

.. sourcecode:: python

   words = []

Work with the class to collect about 5 words.

Now, let's use this list. Remember the ``for`` command? This is another code
block, just like ``if``. ``for`` lets us go over every item inside a list. Let's
remind ourselves what this looks like.

.. sourcecode:: python

   words = ['super', 'exciting']
   for word in words:
      print(word)
   print("Done all words.")


And of course, we see each ``word`` printed on the screen. Remember that we have
to be tabbing. Because ``for`` is a code block, anything tabbed underneath it,
will be run in the loop. Notice how our final ``print`` is only printed once, at
the end, because it is not inside the code block.

Alright! Let's just get some basics done in our game before we move on to the
improving our trivia game. We'll add simple input and use ``if`` and ``else`` to
tell the user if they are right or wrong.

.. sourcecode:: python

   for word in words:
      guess = input("What is your guess?")
      if guess.lower() == word.lower():
         print("You're correct!")
      else:
         print("Sorry, that's not the right word.")

*Give them some time to write out this code and make sure everyone has it
running.*

Great! But there's something really tough about this game .. we're asked to
guess a word and we have no hints or anything! How can we solve this? Well, we
can use loops.

Scrambling a Word Using Loops
-----------------------------

What if we could show only parts of a word and use that as a hint? The great
thing about loops is we can do just that. In Python, a word is actually just a
list of letters. Let's build a new function. We'll put this on the top of our
program, so above your existing code. This function will take a single word as
the parameter and then return the scrambled word. First, let's build the basics
of this function.

.. sourcecode:: python

   def scramble_word(word):
      return word

And then, let's adjust our game loop to *call* this function, so we can print
the scrambled word.

.. sourcecode:: python

   for word in words:
      scrambled = scramble_word(word)
      print("Your Hint Is: %s" % scrambled)
      guess = input("What is your guess?")
      if guess.lower() == word.lower():
         print("You're correct!")
      else:
         print("Sorry, that's not the right word.")

*Review with the class the parts of defining a function. In particular, how the
function is taking a single word and returns a word, and then how we call it.
We're just passing around a variable*

We'll run the program, but we notice something right away -- The word is not
scrambled! Of course not, because our function doesn't do anything. It just
passes the word back. Now that we have everything in place, we can focus on our
``scramble_word`` function.

As we mentioned before, a string in Python is just a list of letters. So let's
improve our scramble word function. What we'll do is go over every letter in the
word, and every second character, we will replace the letter with a ``*``.

*You'll go through implemenenting the below scramble word function step by step.
Recommended process is as follows*

* Implement the ``for`` loop and print out each letter, showing how you can see the breakdown of the word.
* Make a variable called ``new_word`` and add the letter to it, returning ``new_word``. No modificaitons yet
* Finally, add the ``*`` character swapping by implementing the ``counter`` and the ``if`` block.

.. sourcecode:: python

   def scramble_word(word):
      new_word = ""
      counter = 0
      for letter in word:
         counter = counter + 1
         if counter % 2 == 0:
            letter = "*"
         new_word = new_word + letter
      return new_word

Give the students time to fill this out. Mention that they can modify the ``*``
to be anything, including multiple letters, as well as changing the modulus from
``2`` to something else. Let them see how that reacts.

Now, let's run our program! We're getting somewhere. We're now using two loops
in our program, and the game is becoming a little more interesting. Let's see
how we can make our game a little more interesting not with loops, but with some
existing knowledge.

Adding a timer
--------------

Timers are a great way to make any program more interesting. You give a sense of
pace and you make the player think more. Most games you play probably have a
timer for how much time you have left in the level. Python lets us do this
pretty easily.

We'll now introduce a new module we can import. As a reminder, using ``import``
is just a way for us to tell Python that we need this extra piece of code.
Python comes with a lot of code, but we use ``import`` to help it understand
exactly what it needs. Otherwise, if Python included all the possible code and
functions for you right away, it'd make for a very big and slow program! *(This
is not technically accurate, but is probably a decent, high-level explanation of
imports)*

First, we'll add the following to the top of our file.

.. sourcecode:: python

   import time

Then, let's go into our game loop and use the time functions. Let's see what
that looks like:

.. sourcecode:: python

   for word in words:
      scrambled = scramble_word(word)
      print("Your Hint Is: %s" % scrambled)

      # Start off the timer
      start_guess = time.time()

      guess = input("What is your guess?")

      # End the timer, and display how long it took
      end_guess = time.time() - start_guess
      print ("You took %s seconds to guess that" % end_guess)

      if guess.lower() == word.lower():
         print("You're correct!")
      else:
         print("Sorry, that's not the right word.")

*Let them implement, and run it.*

Cool! One thing some students may notice is that the timer number is very big.
We can introduce them to two ways to make this number different. First, we can
use ``round`` to get a number with a certain amount of decimal places, or we can
use ``int`` to make it have no decimal places. Implement either of the following
and show them how it looks now.

.. sourcecode:: python

   end_guess = round(time.time() - start_guess, 2)
   print ("You took %s seconds to guess that" % end_guess)

   # Or.

   end_guess = int(time.time() - start_guess)
   print ("You took %s seconds to guess that" % end_guess)

Amazing! We have a pretty neat game now. Let's do one more thing to really
spruce it up, which will use loops again.

Adding another player
---------------------

Many games have more than one player. Without loops, if we wanted to add more
than one player we'd have to copy and paste the same code over and over again,
depending on how many players we wanted. That's pretty crazy and would make for
some really big Python programs.

Using lists and loops, we can easily add as many players as we want, with only a
few changes of code. First, let's make a new list with our player names.

.. sourcecode:: python

   players = ['Joy', 'Claudia']

Make sure you add yourself, and then either your desk neighbour or anyone you'd
like. Now, let's add the new loop. This loop will begin before most of our game,
so we'll have to *TAB* a lot of code. The best way to do this is after you type
your new ``for`` loop, simply select all the other code and press *TAB*.

Your new code will look something like this:

.. sourcecode:: python

   players = ['Joy', 'Claudia']

   for player in players:
      print("It's %'s turn!" % player)
      for word in words:
         scrambled = scramble_word(word)
         print("Your Hint Is: %s" % scrambled)

         # Start off the timer
         start_guess = time.time()

         guess = input("What is your guess?")

         # End the timer, and display how long it took
         end_guess = time.time() - start_guess
         print ("You took %s seconds to guess that" % end_guess)

         if guess.lower() == word.lower():
            print("You're correct!")
         else:
            print("Sorry, that's not the right word.")

All we added was two lines, but it's very important everything inside ``for
player in players`` is now tabbed. We added a new code block, so we can't forget
to tab. You can spend a moment to show what would happen if we don't tab
(Compile error)

At this point, the class should be mostly over. Give them some time to play with
the program amongst themselves/friends, encouraging them to add more words and
change things up. If there's time, you can add simple score tracking using
variables, and simply adding them up when they are correct, finally printing a
total score when the player loop is complete.
