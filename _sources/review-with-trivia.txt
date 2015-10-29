Review With Trivia (Lesson 5)
#############################

Last week, functions were introduced, and it was a lot to take in. This class
should focus on continuing the education of functions while perhaps introducing
some simpler concepts.

* Introduce Python dictionaries
* Continue education of functions by working through a new exercise, and
  providing time to complete last weeks work if necessary.

Dictionaries
------------

So far we've covered several types of variables. We have ints (numbers),
strings, we've used lists a few times (remember buckets?), but now we want to
introduce dictionaries.

Dictionaries in any programming language are very useful. Their name explains
what they are. In a Python dictionary you have what we call a ``key``, and each
``key`` has a ``value``. To think of it another way, just think that the
dictionary has a list of questions (the key) and their definition (the value).

Why are dictionaries useful? They are excellent for anything we have to look up.
Imagine we made a dictionary for peoples names and their phone numbers. Let's
see what that might look like:

.. sourcecode:: python

    people = {
      'omar': '555-555-5555',
      'amy': '416-200-1010',
    }
  
Our program now has a dictionary of ``people``. So how do we access this?

.. sourcecode:: python

    print(people['omar'])

What if we try to access a person that does not exist in this dictionary?

.. sourcecode:: python

    print(people['bartek'])
    ...
    KeyError: 'bartek'

We can add new items to the dictionary in the same way we access an existing
one, but we use variable assignment. Let's look:

.. sourcecode:: python

  people['bartek'] = '610-001-1000'
  print(people['bartek'])

We no longer have a ``KeyError``, because we have assigned a new definition
(``key``) to this dictionary with the ``key`` of ``bartek``.

What do you think will happen if we change the ``key`` of an existing dictionary
entry?

.. sourcecode:: python

  people['bartek'] = 'not-a-number'
  print(people['bartek'])

Like most of Python, the dictionary has useful functions on it. What if we
wanted to see all the people in our dictionary, or just all the numbers?

.. sourcecode:: python

  print(people.keys())

  # Or, to see all the numbers
  print(people.values())

The dictionary doesn't seem too useful now, but we will see its power in our
upcoming exercise.

Let the students have some time to define a dictionary and play with the
concept. So they can see the results.

Building a Trivia Game
-----------------------

We've learned a lot, a whole lot, in the last several weeks, so we're going to
step back a bit and work through building a simple, but fun game together. 

Our game will be made of a few parts. First, we will need to assign players,
design our questions. After wards, we need to build the game "loop", this is
where we ask the questions and collect points. Finally, we'll need a function to
show scores.

This is a good exercise to go in step with the students. First, let's assign the
players. We'll make this a list, so our game function does not have to worry too
much about how many players we have. Since we're such great programmers, this
will expand without us touching it!

Defining the variables
++++++++++++++++++++++

.. sourcecode:: python

  players = ['Bartek', 'Ivan']

Let's make sure we remind them what lists are (buckets). We will see how useful
they can be shortly.

Then, let's define some questions and answers for our trivia. We'll use our new
knowledge of dictionaries for this!

.. sourcecode:: python

  qa = {
    'Animal in Australia with a pouch?': 'Kangaroo',
    'Tallest building in Toronto': 'CN Tower',
  }

Once they've all had the chance of making these two items, let's start on the
game loop.

The game loop is made up of everything we know, but we may need to review some
of this as it's been awhile. First, we define the function:

Building The Game Loop
++++++++++++++++++++++

.. sourcecode:: python

  def play_trivia(chances=3):
    ....

We explain how our function only takes one optional argument. It is called
``chances`` and will define how many chances each player has before the game is
up. Let's explain how this can be called, with, or without the optional
argument.

Then, let's continue our game. First, we will need a variable to hold scores of
the players. We can use dictionaries for this. Let's make everyone start at 0.

At the end of our function, we will return ``scores``, so let's put that in now
as well.

.. sourcode:: python

  def play_trivia(chances=3):
      scores = {}
      for player in players:
          scores[player] = 0
      return scores

Ok, our game doesn't do much yet, but we're setup to begin asking questions. We
have to write two loops now. One for the amount of chances, and one for each
player. Let's see how that looks.

.. sourcecode:: python

  def play_trivia(chances=3):
      scores = {}
      for player in players:
          scores[player] = 0

      for chance in range(1, chances + 1):
          for player in players:
            print("You're up, %s" % player)

Getting there. We're telling the player it's their turn, but if we run this,
it's just a bunch of prints right away. Our next step is to pick a random
question, share it with the player, and ask their guess.

Let's see what that looks like:

.. sourcecode:: python

  def play_trivia(chances=3):
      scores = {}
      for player in players:
          scores[player] = 0

      for chance in range(1, chances + 1):
          for player in players:
              print("You're up, %s" % player)

              question = random.choice(qa.keys())
              answer = qa[question]
              print("Your question is: %s" % question)

              guess = input("Your guess?")

Important things to share are the usage of ``random.choice`` and ``qa.keys``,
and how that works. Let's break it down for the class. Then, explain how the
random answer can be fetched using ``qa[question]``. For someone new to Python,
this can be very confusing unless explained!

Now, we have a guess. So let's write a function that checks the guess by getting
the computers answer and comparing it to guess.

Python Thinks Differently About Words
+++++++++++++++++++++++++++++++++++++

.. sourcecode:: python

  def check_guess(answer, guess):
    guess = guess.lower()
    real_answer = real_answer.lower()
    return guess == real_answer

Ok, what's going on here? Why do we ``lower`` the answers? This is a simple
trick that will ignore capitals and all case when checking the answer. This is
because Python cares about case. For Python, the words ``Hello`` and ``hello``
are different! To us, they are the same.

Now, let's use our new ``check_guess`` to check if they are correct, and give
them some points!

.. sourcecode:: python

  def play_trivia(chances=3):
      scores = {}
      for player in players:
          scores[player] = 0

      for chance in range(1, chances + 1):
          for player in players:
              question = random.choice(qa.keys())
              answer = qa[question]
              print("You're up, %s" % player)
              print("Your question is: %s" % question)

              guess = input("Your guess?")
              is_correct = check_guess(answer, guess)
              if is_correct is True:
                  print("You're correct! 1 point!")
                  scores[player] += 1
              else:
                  print("Oops! Not quite!")
      return scores

Wrapping Up
+++++++++++

And now we have scores! Finally, we can wrap things up by writing a simple
function to display the scores.

.. sourcecode:: python

    def display_scores(scores)
        print(" ======== SCORE BOARD ========== ")
        for player, score in scores.items():
            print ("%s = %s " % (player, score))

And finally, we put it all together:

.. sourcecode:: python

    import random

    qa = { ... }
    players = [ ..... ]

    scores = play_trivia(chances=3)
    display_scores(scores)

