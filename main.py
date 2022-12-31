"""
This is a simple program that prompts user to enter
the name of a place and their pet which input upon being
captured is concatenated and used to suggest a possible
band name.

It demonstrates:
1. The use of the print function which displays
information onto the screen
2. The use of the output function which prompts and allows
user to submit information.
3. The use of f strings which allow for different data types to
be output by the print function.
4. Use of variables to store and retrieve information.
"""

print("Welcome to the Band Name Generator!\n")

city = input("Whats the name of the place you grew up in?\n")

pet = input("What is the name of your pet?\n")

print(f"Your band could be {city} {pet}.")
