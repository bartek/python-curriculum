Functions (Lesson 4)
####################

The objective of this class will be:

* Introduce functions
* Clear understanding of why we need functions as our programs grow.
* Variable Scope

Begin by congratulating the students on their knowledge of the Python
fundamentals. The first three weeks have been quick, but have gone over very
important parts of Python.

Now, we'll begin noticing our programs grow, and we might begin repeating
ourselves. Enter functions

Tell the class they've already seen one of the ways functions are re-used.

Remember when we did this?

.. sourcecode:: python

   import random

   computers_choice = random.randint(0, 100)

We re-used a function that was written by people just like you, and this
function was added to the Python "library".

Think of functions as chunks of code that tell Python to do something. They are
one way to re-use something. We can tell our programs to use functions again and
again.

When you're writing small programs, functions are handy. Once you start writing
long, more complicated programs, like games, functions are *essential*!

Writing Our First Function
--------------------------

Let's write our own function, and understand how it is built.

.. sourcecode:: python

   def say_name(name):
      print("Hello %s" % name)

Ok, let's break this down. A function is made up of three parts: *name*,
*parameters*, and the *body*.

The name of this function is ``say_name``. We generally want to try and name
functions to match what they are doing. The parameters of this function is one
variable, ``name``, and the body is the ``print`` statement.

Finally, we will notice a new way of printing variables. The ``%s`` is just a
place holder for the variable at the end of the line.

Let's use our function.

.. sourcecode:: python

   say_name("Bartek")

When we run this, we will see it prints ``Hello Bartek``.

A function can take more than one argument. It can take as many as your computer
can handle, really.

.. sourcecode:: python

   def say_full_name(first_name, last_name):
      print("Hello %s %s" % (first_name, last_name))

Ask the class if anyone can guess how we would call this function. Then let's
look at the answer. Additionally, we point out another use-case of our ``%s``
placeholder.

.. sourcecode:: python

   say_full_name("Bartek", "Ciszkowski")

Of course, these *parameters* for a function can live in variables.

.. sourcecode:: python

   fname = "Bartek"
   lname = "Ciszkowski"
   say_full_name(fname, lname)

And we will see the same result, ``Hello Bartek Ciszkowski``.

Finally, most functions return something. Today we will also learn the
``return`` statement. Returning information is useful because we can put it back
into a variable, and then use that result in another part of our program. Let's
look at what that looks like.

.. sourcecode:: python

   def savings(pocket_money, paper_route, under_couch):
      return pocket_money + paper_route + under_couch

Now, we can call this function with our three ways we save money, and see what
the result is. Let's try it.

.. sourcecode:: python

   pocket_money = 10
   paper_route = 24
   under_couch = 2

   my_savings = savings(pocket_money, paper_route, under_couch)

   # Or we can call the function without variables, of course.

   my_savings = savings(11, 12, 1)

And finally, we can ``print(my_savings)`` and see that our ``savings`` function
did the work for us to calculate our savings.

Allow the students to try some examples of ``return``'ing data from a function.
Challenge here can be to write a function which returns someones name, but in
reverse (last name first, then first name)!

Variable Scope in Functions
---------------------------

Now that we are using functions and our programs are getting larger. We have to
be aware of something called *scope* in Python. Scope is important, because
Python only trusts variables for a specific function, within a certain area.
Let's look at an example:

.. sourcecode:: python

   def scope_test():
      pencils = 10
      pens = 5
      return pens + pencils

   print(scope_test())

Let's run this, and see the result. Everything looks good right? Now, let's ask
the class what would happen if we did something like so:

.. sourcecode:: python

   def scope_test():
      pencils = 10
      pens = 5
      return pens + pencils

   print(scope_test())
   print(pens)

This is because if we look at the code. ``pens`` is only defined inside the code
block for the ``scope_test`` function. So, nothing else in the Python program
has access to it. This is nice because when our programs get really big, we can
re-use the same name for variables inside functions without worry about them
conflicting with each other.

A More Complex Function
-----------------------

Now, so far, we have had simple functions that don't really do much more than
our brains can do. It's pretty easy to count some simple pocket change, so let's
make a function that does something our brains would have a hard time doing!

So let's suppose we're building a car that goes to the future. It's a time
travel car. We can build this car out of old cans we find. We know we can
flatten 2 cans a week to create the panels for our car, and we need to flatten
500 cans to complete the car.

We can easily write a function to figure out how long it will take to flatten
all 500 cans. Let's see what that looks like.

.. sourcecode:: python

   def timetravel_car_building(cans_per_week):
      total_cans = 0
      for week in range(1, 53):
         total_cans = total_cans + cans
         print("Week %s = %s cans" % (week, total_cans))

Let's try it out! First with 2 cans per week. Is it enough? Let's figure out how
many cans per week we need to flatten to build our car within a year.

The students will figure this out by writing out the function, and trying
different values.

Exercise
--------

Let's use our new knowledge of functions to help us make an inter-planetary
bank! Our bank will be pretty simple, allowing us to deposit, withdraw, and see
our space cash balance.

We'll start the students off with the deposit function, and an overview of  the
application, then leave them to implement the ``withdraw`` and ``balance``
functions. They can modify the banks theme and questions as they wish, or even
add more functions if they can think of such!

.. sourcecode:: python

   print("Welcome to Space Bank! For all your inter-galactic needs!")

   total_cash = 0

   def deposit(current_cash, amount):
     return current_cash + amount

   while True:
     print("1 - Deposit")
     print("2 - Withdrawal")
     print("3 - Space Cash Balance")
     print("Any other key to exit")

     command = str(input("What would you like to do? "))
     if command == "1":
       amount = int(input("How much space bucks would you like to deposit? "))
       total_cash = deposit(total_cash, amount)
       print("Thank you! You now have %s " % total_cash)
     else:
       break

Bonus Challenges:

   * Add a function to that tells the user what temperature is. But because
     we're sneaky, let's use ``random`` like we did from other classes to
     randomly provide the weather.
   * Add restrictions to your ``deposit`` and ``withdraw`` functions so that
     they cannot deposit negative values, and they cannot withdraw more than
     they have, respectively.
