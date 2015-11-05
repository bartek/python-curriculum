Back to Turtles (Lesson 6)
##########################

After some fast paced weeks of learning the fundementals of Python, it's a good
opportunity to go back to playing with Turtle. We used Turtle in the first week
with some very basic commands, before we really understood much of Python. Now,
we can apply some of our new knowledge to explore the possibilities of this
module.

Goals for this week:

* Allow time for finishing up the activity in Lesson 5 if not completed.
* Going back to the turtle module, and applying our knowledge of functions, loops, variables, and data structures.

Starting with the basic square
-------------------------------

We already learned how to use turtle in some basic manners, but it's been
awhile. So let's take a look at what that looks like.


.. sourcecode:: python

   import turtle
   t = turtle.Turtle()
   t.shape('circle')

   t.forward(50)
   t.left(90)
   t.forward(50)
   t.left(90)
   t.forward(50)
   t.left(90)
   t.forward(50)

This is pretty repetitive. Ask the class if anyone can see the pattern and point
it out.

We can improve this and make it less repetitive by using loops. Now that we've
identified the pattern (forward, left, 4 times) we can re-write our code as a
loop:

.. sourcecode:: python

   for x in range(1, 5):
      t.forward(50)
      t.left(90)


The benefits here are huge! Right away, we can adjust the size of our square
with one simple change (Changing ``t.forward``), rather than doing it four
times, for each time that function is used.

Let's go one step further and make this a function, so we can easily use it
later.

Ask the class if anyone can tell me how I write a function. Does a square
function take parameters?

.. sourcecode:: python

   def square(size=50):
      for x in range(1, 5):
         t.forward(size)
         t.left(90)


We must note here that ``size`` is the parameter that defines how large each
line in our square will be, thus it will define how large the overall square
will be.

Great! Let's make sure we save this as we'll use it later.

Drawing Stars
-------------

Squares are alright, but they are pretty simple, and not too exciting. So let's
try and ramp it up. How would we draw a star?

Ask the class: How many points does a typical star have?

Drawing a star should be very similar to drawing a square. We'll want to draw
several lines (8, perhaps), and turn left, but not 90 degrees. What's a possible
good number?

In the end, the class may help you get a different solution but effectively, you
want something like so:

.. sourcecode:: python

   for x in range(1, 9):
      t.forward(100)
      t.left(225)

What if we used a smaller angle (``175`` instead of ``225``), and looped many
more times? Let's try a few examples and see the results.

Eventually, let's save this star as another function, named ``star``

Conditionals in our shapes
-------------------------

Using very similar code to our star, we can create a large variety of shapes. We
can even go further and use conditionals to create some pretty cool shapes.

Let's write out this function:

.. sourcecode:: python

   for x in range(1, 19):
      t.forward(100)
      if x % 2 == 0:
         t.left(175)
      else:
         t.left(225)

For the class, the conditional itself should be pretty straight forward. We've
done this and they understand the concepts. But what is the ``%`` symbol?

Let's explain modulus at a high level. Essentially, it's saying *"What is the
amount left over when you divide the numbe rin variable x into two equal
parts?"*

After explanation, allow the students to guess what might be drawn, and then run
it.

Allow them to write the code for this as well, modifying it as they wish, and
then making that a function as well.

Using Help to Colour Our Shapes
--------------------------------

So now we have code that will draw us squares and a couple of neat looking
stars. But how do we colour them in?

Let's introduce them to navigating some basic documentation. On trinket.io,
there's the option to see *Available Python Modules*. The direct link leads to
`https://trinket.io/docs/python <https://trinket.io/docs/python>`_.

Working together, we'll find the ``turtle`` module in this documentation, all
the while explaining how we can use this.

Finally, we will find turtle and go through the functions. Eventually
``begin_fill`` catches our eye. Let's read it out loud to the class and
understand how it works. Then, we try it out.

.. sourcecode:: python

   import turtle
   t = turtle.Turtle()
   t.shape('circle')
   t.begin_fill()
   square()

And we called our square function and notice  it's now been filled in! We try a
few more movements but notice something is happening, the fill has not stopped,
and our entire screen is covered in colour.

We look back at the documentation and we find ``end_fill``, and apply it to our
code.

.. sourcecode:: python

   import turtle
   t = turtle.Turtle()
   t.shape('circle')
   t.begin_fill()
   square()
   t.end_fill()


Working with the class, let's add ``filled`` as an optional parameter to the
square and star functions. Let's make the default ``False``, so we don't always
have to tell Python to fill or not.

Then, we can apply simple conditional logic in each of our functions to decide
whether to fill or not.

.. sourcecode:: python

   def square(size=90, filled=False):
      if filled == True:
         t.begin_fill()
      ....
      if filled == True:
         t.end_fill()

Exercise
--------

Looking back at todays work, we now have an ample supply of functions that
we can use over and over again in our code to draw interesting patterns and make
a piece of art.

Before we get to playing with these, let's challenge the class to try and create
their own shape. 

We'll specifically talk about the octagon. It's an eight sided shape, so we can
use the same logic we used for squares and stars to draw it. This should be
simple, but it'll really test their knowledge of functions and loops, and
everything we just did.


.. sourecode:: python

   import turtle
   t = turtle.Turtle()
   t.shape('circle')

   for x in range(1, 9):
     t.forward(90)
     t.left(45)

Additionally,  challenge them to try and use the documentation to find out how
to change the colour, and have them apply that in their code, in whatever way
they wish. Ideally, they can make it another parameter in their draw functions.

If they finish the activity early, allow for them to have some time playing with
the various functions they built, and introduce them to ``penup`` in the turtle
module, so they know how to "skip" along the screen.
