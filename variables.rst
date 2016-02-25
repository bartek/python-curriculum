Variables & Iteration (Lesson 2)
################################

It's time to begin digging into the core of the Python programming language!
Understand the basics and begin answering many questions that filled the
students minds in the last lesson.

We introduce the class to mention today we're going to talk about variables.
They are one of the main building blocks of any program, and are very important
in understanding.

Imagine variables are like labels. They describe, to the computer, a place to
store information such as numbers, text, lists of numbers and text, and so on.
Let's share a variable declaration on the screen.

.. sourcecode:: python

   colour = "red"

Here, we explain that we have stored the *String red*, in the variable
``colour``. We identify that a *String* in Python is wrapped in double quotes.
We can also use single quotes, but all examples will use double quotes.

We can print the variable onto the screen, using the ``print`` function.

.. sourcecode:: python

   colour = "red"
   print(colour)


We explain why I chose the variable name ``colour``. I can change *red* to
*green*, but if I changed the variables value to *Fred* it doesn't really
signify a colour anymore. Re-iterate that variables are like labels. We want
them to match the value we have put in. So for *Fred*, a better variable name
might be ``first_name``.

Let's share that variables can be numbers. Computers are really good at Math, so
let's see how the computer handles this operation. Can anyone guess the answer?
(Simple way to get interaction with the class)

.. sourcecode:: python

   score = 100
   score = 100 / 2 - 25
   print(score)

Finally, let's share that variables can be used together, and joined using the
``+`` operator. Another example:

.. sourcecode:: python

   first_name = "Bartek"
   last_name = "Ciszkowski"
   print("Hello, my name is " + first_name + " " + last_name)

We share that the ``+ " " +`` is joining my variables with a string. Explain why we
must have an string with just a space in it. Show the students what happens if
we simply had ``first_name + last_name``.

Numbers, Strings, And More!
---------------------------

If you've been looking closely, you'll see that we used variables which we wrap
in quotes (``"``), and variables that are just plain numbers.

In many programming languages, we have to tell the computer what these are.
Python guesses for us based on how we type it. Why is it important for the
computer to know what type of variables we are using? Well, it needs to know the
best way to do what you want with the variable. Let's look at the following
example:

.. sourcecode:: python

   print(20 + 16)

   # vs.

   print("20" + "16")

We need to understand that any variable *value* wrapped in quotes is a *String*,
and a number with no decimals is an *Integer*. As you can see, Python treats
each differently.

Ask the students if they can guess what the term is for a number that looks like
this: ``105.10``.

Provide the students time to enter their own variables, join strings, and fiddle
with these new concepts.

Introducing Lists
-----------------

Lists are very important in any programming language, as they let us put
information into a more structured way. We can think of lists as buckets, as
they can contain many types of strings, numbers, or other variables. 

Let's see an example of a list using our bucket as an example. We'll print the
list and see what it looks like on the screen.

.. sourcecode:: python

   # This list was provided by the students of the class
   bucket = ['candy', 'water', 20, 'chocolate', 'bucket']
   print(bucket)

Lists can be a collection of any kind of items. We point out that we have four
strings and a number. Each of these items can be accessed using a special
syntax.  Ask the students when the below code is run, what will be printed?

.. sourcecode:: python

   bucket = ['candy', 'water', 20, 'chocolate', 'bucket']
   print(bucket[1])

Of course, most will guess ``candy``. We explain that in Python, and in most
computers, counting starts at 0, so the result is ``water``.

Let's share how we can change lists, by adding to them.

.. sourcecode:: python

   bucket = ['candy', 'water', 20, 'chocolate', 'bucket']
   print(bucket)
   bucket.append('skittles')
   print(bucket)

Let's explain why each ``print`` is a little different. This is because Python
is reading from top to bottom, so the change in our bucket doesn't happen in the
first ``print``.

Iteration
---------

Finally, before the last part of the lesson, we want to introduce iteration. We
do this by iterating over the list.

.. sourcecode:: python

   bucket = ['candy', 'water', 20, 'chocolate', 'bucket']
   for item in bucket:
      print(item)

This is a lot to take in, but we introduce the colon (``:``) and how it tells
Python that next line (and perhaps more) are a new section of code. Each new
section of code needs to be spaced like we see. We explain that ``tab`` can be
pressed when we need to do this.

We'll better understand when and where Python needs to tab in coming lessons.

For now, we focus on the result of this code. We see that each item in the
``bucket`` is printed. What if we replace the ``print(item)`` with
``print(bucket)``? Let's see what happens, and ask if someone understands why.

Finally, we jump back to ``turtle``. As mentioned in the introduction, we want
to be as visual as possible, and ``turtle`` is a great way to achieve this.

We're going to use what we learned about variables and lists to give our turtle
a list of commands. Let's share the following code example (Thanks, `trinket.io
<http://trinket.io>`_):

.. sourcecode:: python

   import turtle
   tina = turtle.Turtle()
   tina.shape('turtle')

   number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

   tina.color('green')
   for number in number_list:
      tina.forward(number * 10)
      tina.left(60)

Let's display what this does on the screen. We'll see our turtle spinning around
in an ever-growing circle. Fiddle with the ``number_list`` a bit, interactively
with the class and see the results.

To wrap up the lesson, allow the students to enter the code and try their own
commands, number list, and anything else that inspires them. They may need some
help to really wrap their mind around these new concepts but as they type it out
more and see the results, it will begin to click.

Let them continue playing with this code until the end of the class.
