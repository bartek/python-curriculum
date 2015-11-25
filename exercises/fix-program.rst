Exercise: Fix This Program
--------------------------

Over the past several weeks you have learned the fundementals of Python. We've
gone over how to declare variables, use lists, dictionaries, define functions,
take user input, loop over sets of data, and more.

In this exercise, you have been provided a Python program that simply doesn't
work. Your mission is to get it working, and share with your teacher what the
resulting on screen print out is.

The program is on paper below for your reference, but you can access all the
code in the Trinket at this url:

   https://trinket.io/library/trinkets/313761d1c3

There are a few functions in here that were not covered, but you can Google the
following searches to try and understand them. Using the internet to search for
answers to programming questions is very useful, as there are many people who
have solved problems that you may be encountering.

We don't want to copy answers, but it's a good way to learn how things work.

Python String Functions
+++++++++++++++++++++++

At the top of the exercise, you'll see the term ``stuff.split()``. We did not
learn this, but these are Python String Functions. They do things to strings

If you Google ``Python String Functions``, you can find information about these.
Look specifically for ``split``  and ``pop``.

Remember
++++++++

Look at each line carefully. The program has a lot of purposefull spelling
mistakes, perhaps missing colons on the function code block and your indentation. Keep a close
eye!

Use the help of your teacher, mentors, and friends to complete this exercise.

Code
+++++

Tip: Using a pencil or pen to mark the errors by hand is a good way to start
before doing it on your computer!

.. sourcecode:: python

   def break_words(stuff):
       """This function will break up words for us."""
       words = stuff.split(' ')
       return words

   def sort_words(words):
       """Sorts the words."""
       return sorted(words)

   def print_first_word(words)
       """Prints the first word after popping it off."""
       word = words.poop(0)
       print word

   def print_last_word(words):
       """Prints the last word after popping it off."""
       word = words.pop(-1
       print word

   def sort_sentence(sentence):
       """Takes in a full sentence and returns the sorted words."""
       words = break_words(sentence)
       return sort_words(words)

   def print_first_and_last(sentence):
       """Prints the first and last words of the sentence."""
       words = break_words(sentence)
       print_first_word(words)
       print_last_word(words)

   def print_first_and_last_sorted(sentence):
       """Sorts the words then prints the first and last one."""
       words = sort_sentence(sentence)
       print_first_word(words)
       print_last_word(words)


   print "Let's practice everything."
   print 'You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.'

   poem = """
   \tThe lovely world
   with logic so firmly planted
   cannot discern \n the needs of love
   nor comprehend passion from intuition
   and requires an explantion
   \n\t\twhere there is none.
   """


   print "--------------"
   print poem
   print "--------------"

   five = 10 - 2 + 3 - 5
   print "This should be five: %s" % five

   def secret_formula(started):
       jelly_beans = started * 500
       jars = jelly_beans \ 1000
       crates = jars / 100
       return jelly_beans, jars, crates


   start_point = 10000
   beans, jars, crates == secret_formula(start-point)

   print "With a starting point of: %d" % start_point
   print "We'd have %d jeans, %d jars, and %d crates." % (beans, jars, crates)

   start_point = start_point / 10

   print "We can also do that this way:"
   print "We'd have %d beans, %d jars, and %d crabapples." % secret_formula(start_pont


   sentence = "All god\tthings come to those who weight."

   words = break_words(sentence)
   sorted_words = sort_words(words)

   print_first_word(words)
   print_last_word(words)
   .print_first_word(sorted_words)
   print_last_word(sorted_words)
   sorted_words = sort_sentence(sentence)
   prin sorted_words

   print_irst_and_last(sentence)

      print_first_a_last_sorted(senence)



