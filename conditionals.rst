Conditional Statements (Lesson 3)
#################################

Having variables and a basic understanding of iteration under our belt, we need
to dive into logic. The objectives of this class will be:

* Introduction to conditional statements
* Clearer understanding what signifies a block of code in Python
* The difference between strings and numbers (important in conditionals!)

Conditional statements can be seen as a way to ask questions to the computer.
Often, we want our program to do something differently depending on something
else. For example, if the person using our program was younger than 16, we would
not ask them if they have a Drivers License yet.

Let's look at how a conditional statement looks like in Python:

.. sourcecode:: python

   age = 11
   if age > 20:
      print("You are pretty old.")

Remember our ``for`` loop? There are a few similarities. This ``if`` statement
also ends with a colon (``:``), and the ``print`` is tabbed inside.

Code Blocks
-----------

It's important we begin understanding how code blocks work. Let's look at our
first example again, with a couple more lines added to it.

.. sourcecode:: python

   age = 11
   if age > 20:
      print("You are pretty old.")
      print("Maybe you need a different class.")
      print("Are you finished school?")

   print("See you later.")

When you look closely, we can see that out of the four ``print`` statements, one
of them is not aligned like the others. Why is this?

This is because the first three ``print`` statements are part of the ``if`` code
block. This means we will only see those if the ``age`` is over 20. Let's run
the program and see what happens.

You will notice that because ``age`` is not over 20, we only see the text *See
you later.*

Now, once you are in a code block you don't want to really change your tabbing.
For example, let's look at this:

.. sourcecode:: python

   age = 11
   if age > 20:
      print("You are pretty old.")
      print("Maybe you need a different class.")
         print("Are you finished school?")

Instead of going back to the left, we went further right with the third
``print``. Ask the students what they think will happen here.

You will present to the class an ``IndentationError``. This can be explained
because we never started a new code block (with an ``if`` or a ``for``, which
both end in colons!) so Python doesn't allow it.

Allow the students to write down the example in their own editor and try it out.

More Comparisons
----------------

Now that we have an understanding of code blocks, let's look at more ways to
compare. We have an assortment of special characters that compare one thing to
another, they are:

.. sourcecode:: python

   ==  # Equal to
   !=  # Not equal to
   >   # Greater than
   <   # Less than
   >=  # Greater than or equal to
   <=  # Less than or equal to

For example, if you are 12 years old, the following code would print "You're
12!"

.. sourcecode:: python

   age = 12
   if your_age == 12:
      print("You're 12!")

Allow the students to try a few of these on their own, and provide some examples
for the class through an interactive session, going over some of the operators.

Now, we can also use conditionals to do something when a condition is not met.
Let's look at what this looks like in an example:

.. sourcecode:: python

   keys = 0
   if keys > 0:
      print("You opened the secret door.")
   else:
      print("You need a key to open this secret door.")

Because we don't have any ``keys``, we tell the user that they need a key to
open the door. Try changing ``keys`` to a positive number, and see the
difference.

We can get even more creative by using the ``elif`` statement to do what is
called an "else-if conditional". Let's see what that looks like.

.. sourcecode:: python

   score = 20
   if score == 0:
      print("You need more points!")
   elif score == 20:
      print("You have some points.")
   elif score == 100:
      print("You have all the points!")

Now our programs are getting pretty complex! When we first run this wee see *You
have some points.*. Then, if we change ``score`` to equal ``100``, we will see
*You have all the points!*.

What happens when we change score to say, ``10``? We see nothing is printed.
This is because none of our conditionals match our options. Remember the
``else`` condition we used earlier? We can use that in this example to make our
computer say something if nothing else matches.

.. sourcecode:: python

   score = 20
   if score == 0:
      print("You need more points!")
   elif score == 20:
      print("You have some points.")
   elif score == 100:
      print("You have all the points!")
   else:
      print("Ok, you have " + score + " points")

Types Of Variables
------------------

So far, we have only compared numbers. Remember, that in Python numbers and
strings are different things. The following two are different:

.. sourcecode:: python

   print(2)
   print("2")

The first is a number, and the second, wrapped in quotes, is a string. This is
very important when we compare variables, as it can really confuse Python. Let's
take a look:

.. sourcecode:: python

   age = '12'
   if age == 12:
      print("You're 12 years old!")

When we run this, we will see that Python never tells us we're 12 years old. If
we look closely, we see, that we set ``age`` to be ``'12'``, a string. Not a
number! When we change ``age`` to a number, our code will work.

Exercise
--------

Let's build a simple guessing game using our new knowledge of conditional
statements. The computer will pick a random number that you won't know, and then
we have to try and guess it. The computer will tell us if we're too high or too
low. Let's look at how this code will look like:

.. sourcecode:: python

   import random

   computers_choice = random.randint(0, 100)

   while True:
      guess = int(input("What is your guess?"))
      if guess > computers_choice:
         print("Your guess is too high!")
      elif guess < computers_choice:
         print("Your guess is too low!")
      elif guess == computers_choice:
         print("You're right!")
         break

There are some new things here. Like ``while`` and ``input``, but don't worry
too much about that. We will learn more what those mean, the important part is
we understand our conditionals.

For bonus, ask the students if they can figure out how ask for the persons name
and instead of saying ``Your``, use their knowledge from previous weeks to
reference the person by their name.

For further bonus (Generally useful if someone is ahead in class), can you make the conditional statements more accurate? Maybe instead of just saying *Your guess is too high!* you can add more conditions, so we can tell the user they are *WAY* too high, or *WAY* too low, and so on.
