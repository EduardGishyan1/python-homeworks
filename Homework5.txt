# Exercise 1

# print("Hello world!")
# print("Hello Again")
# print("I like typing this")
# print("This is fun.")
# print("Yay! Printing.")
# print("I'd much rather you 'not' .")
# print('I "said" do not touch this')
# print("Another line")

# Exercise 2

# A comment, this is so you can read your program later.
# Anything after the # is ignored by python.

# print("I could have code like this.") # and the comment after is ignored

# # You can also use a comment to "disable" or comment out code:
# # print("This won't run.")

# print("This will run.")

# # Exercise 3

# print("I will now count my chickens:")

# print("Hens", 25 + 30 / 6)
# print("Roosters", 100 - 25 * 3 % 4)
# print("Now I will count the eggs:")
# print(3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6)
# print("Is it true that 3 + 2 < 5 - 7?")
# print(3 + 2 < 5 - 7)
# print("What is 3 + 2?", 3 + 2)
# print("What is 5 - 7?", 5 - 7)
# print("Oh, that's why it's False.")
# print("How about some more.")
# print("Is it greater?", 5 > -2)
# print("Is it greater or equal?", 5 >= -2)
# print("Is it less or equal?", 5 <= -2)

# # Exercise 4

# cars = 100
# space_in_a_car = 4.0
# drivers = 30
# passengers = 90
# cars_not_driven = cars - drivers
# cars_driven = drivers
# carpool_capacity = cars_driven * space_in_a_car
# average_passengers_per_car = passengers / cars_driven

# print("There are", cars, "cars available.")
# print("There are only", drivers, "drivers available.")
# print("There will be", cars_not_driven, "empty cars today.")
# print("We can transport", carpool_capacity, "people today.")
# print("We have", passengers, "to carpool today.")
# print("We need to put about", average_passengers_per_car,"in each car.")

# # Exercise 5

# name = 'Zed A. Shaw'
# age = 35 # not a lie
# height = 74 # inches
# weight = 180 # lbs
# eyes = 'Blue'
# teeth = 'White'
# hair = 'Brown'

# print(f"Let's talk about {name}.")
# print(f"He's {height} inches tall.")
# print(f"He's {weight} pounds heavy.")
# print("Actually that's not too heavy.")
# print(f"He's got {eyes} eyes and {hair} hair.")
# print(f"His teeth are usually {teeth} depending on the coffee.")
#  # this line is tricky, try to get it exactly right
# total = age + height + weight
# print(f"If I add {age}, {height}, and {weight} I get {total}.")

# # inch to cm

# inch = input("Convert inches to cm: ")

# if inch.replace('.', '', 1).isdigit():
#     print("cm =", float(inch) * 2.54)
# elif float(inch) < 0:
#     print("Enter a valid number")
# else:
#     print("Enter a number")

# # pound to kg

# pound = input("Convert pound to kg: ")

# if pound.replace('.', '', 1).isdigit():
#     print("kg =", float(pound) * 0.45359237)
# elif float(pound) < 0:
#     print("Enter a valid number")
# else:
#     print("Enter a number")



# # Exercise 6

# types_of_people = 10
# x = f"There are {types_of_people} types of people." # string
# binary = "binary" # 1
# do_not = "don't" # 2
# y = f"Those who know {binary} and those who {do_not}." # string
# print(x)
# print(y)
# print(f"I said: {x}") # string
# print(f"I also said: '{y}'") # string
# hilarious = False
# joke_evaluation = "Isn't that joke so funny?! {}" # string
# print(joke_evaluation.format(hilarious))
# w = "This is the left side of..." # 3
# e = "a string with a right side." # 4
# print(w + e) # connect 2 side of strings

# # Exercise 7


# #print("Mary had a little lamb.")
# #print("Its fleece was white as {}.".format('snow'))
# #print("And everywhere that Mary went.")
# #print("." * 10) # what'd that do?

# #end1 = "C"
# #end2 = "h"
# #end3 = "e"
# #end4 = "e"
# #end5 = "s"
# #end6 = "e"
# #end7 = "B"
# #end8 = "u"
# #end9 = "r"
# #end10 = "g"
# #end11 = "e"
# #end12 = "r"
# # watch end = ' ' at the end. try removing it to see what happens
# #print(end1 + end2 + end3 + end4 + end5 + end6, end=' ')
# #print(end7 + end8 + end9 + end10 + end11 + end12)

# # Exercise 8

# formatter = "{} {} {} {}"
# print(formatter.format(1, 2, 3, 4))
# print(formatter.format("one", "two", "three", "four"))
# print(formatter.format(True, False, False, True))
# print(formatter.format(formatter, formatter, formatter, formatter))
# print(formatter.format(
# "Try your",
# "Own text here",
# "Maybe a poem",
# "Or a song about fear"
# ))

# # Exercise 9

# # Here's some new strange stuff, remember type it exactly.

# days = "Mon Tue Wed Thu Fri Sat Sun"
# months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"

# print("Here are the days: ", days)
# print("Here are the months: ", months)

# print("""
# There's something going on here.
# With the three double-quotes.
# We'll be able to type as much as we like.
# Even 4 lines if we want, or 5, or 6.
# """)

# # Exercise 10

# tabby_cat = "\tI'm tabbed in."
# persian_cat = "I'm split\non a line."
# backslash_cat = "I'm \\ a \\ cat."

# fat_cat = """
# I'll do a list:
# \t* Cat food
# \t* Fishies
# \t* Catnip\n\t* Grass
# """
# print(tabby_cat)
# print(persian_cat)
# print(backslash_cat)
# print(fat_cat)

# sentence = "special characters: \\, \', \", \a, \b, \f, \n, \r, \t, \v, \N{SNOWMAN}, \U0001F604, \u2764, \105, \x61"

# print(sentence)

