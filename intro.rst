Introduction (Lesson 1)
#######################

First class! In this initial lesson, we aren't going to be too formal. We want
to achieve the following:

* Introduce names (teachers, mentors, students)
* Get every student setup with Python
* Be able to begin imagining possibilities for their own Python-based projects
* Begin understanding the concepts of computational creation
* Begin establishing a culture of fearlessness, exploration, and peer collaboration

Introducing Python
------------------

After introductions of teachers and students, it's time to introduce Python!
Python is fun to learn, feels a little bit like learning English, and as well,
it's a language used in real life businesses. We can share how companies like
NASA, Google, and Facebook use Python, as well that it's taught in high school
and university.

Even if you don't want to become a computer programmer, learning a programming
language like Python will refine your logical thinking, increase creativity, and
teach you not to fear a computer.

Introducing the toolset
-----------------------

Depending on the lab environment, you can either install Python and the Python
Tkinter toolkit, or use the online tools like `trinket.io <http://trinket.io>`_

This curriculum recommends using `trinket.io <http://trinket.io>`_, as it
provides a great interface for seeing code and the results all in one screen.
They support registered accounts, allowing the students to save their work and
share it when at home.

First Code Example
------------------

We'll want to take advantage of Python's ``turtle`` module as much as we can.
Thus, we introduce the first Python example is using this module. For the first
few weeks, we'll focus on bringing each lesson back to the ``turtle`` module, to
provide that visual feedback.

This snippet can also be found on the ``trinket.io`` website. Get this code on
the screen using Trinket, so we can see the results beside the code.

.. sourcecode:: python

   import turtle
   tina = turtle.Turtle()
   tina.shape('turtle')

   tina.penup()
   tina.forward(20)
   tina.write("Why, hello there!")
   tina.backward(20)

Run this code and share it with the class. There are many concepts in these few
lines that the students will not understand right away, but go over each line,
and simply say it out loud.

We don't need to get into how ``import`` works, or why there are brackets where
they are. Simply identify how ``tina.forward(20)`` affects the turtle's movement
in a specific direction.

Then, leave the code up on the screen in front of the class and let the students
try it themselves.

Students may miss brackets or have certain symbols (``=``) within incorrect
spots. Help them resolve the error, but there's no need to get too deep into why
that happened just yet.

Eventually, all the students will have the code running. Play with the code
again in front of the class, adjusting the values. Add more movement.

Introduce the ``left`` and ``right`` functions on the ``turtle`` module. Allow
the students to try various implementations throughout the rest of the class.

As the class  comes to an end, ensure everyone saves their work. We want to
promote the ability to look back at previous work, as well as being able to
share it with their friends and family outside of the class (Assuming an online
tool like ``trinket.io`` was used).
