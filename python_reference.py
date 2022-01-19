#############
# IMPORTING #
#############

# Regular imports
import dataclasses
from dataclasses import dataclass

# You can rename the things you import with the "as" keyword
import os as operating_system
from os import path as p

##############################
# VARIABLES / BUILT-IN TYPES #
##############################

# Showing variable declarations
num = 2
string = "aaa"

# Print out the string
print(string)

# Can add string to concatenate them
print("AAA" + string)

# But you have to convert to string before adding
print("AAA" + string + str(num))

# By putting the letter f in front of the string, you can insert other variables into
# the middle of the string and avoid this problem
# <--- will cast everything to strings for you
print(f"Num: {num}, String: {string}")

# Lists don't care about types and are not restricted to one type
list_a = [num, string, "5", 33]

# You can also define a list vertically like this
list_a = [
    num,
    string,
    "5",
    33,  # Trailing comma is standard practice in case you want to add more items later
]

# Access parts of a list like an array
print(list_a[0])

# Or, access a sublist using "splice" notation
print(list_a[1:])  # All items from index 1 and after (including index 1)
print(list_a[:2])  # All items from before index 2 (not including index 2)
# All items from index 1 to 2 (including index 1 but not index 2)
print(list_a[1:2])

# Dictionaries are like lists with key-value pairs. They are maps from SW1.
# Keys must be unique but their associated values do not have to be unique
dict_a = {
    "A": 1,
    "B": 1,
    "C": 2,
    "D": 3,  # Same thing about trailing commas here
}

# Access keys from the dictionary
print(dict_a["A"])
print(dict_a["D"])

##########################
# CONDITIONALS AND LOOPS #
##########################

# True and False are capitalized in Python
t = True
f = False

# if statements use words instead of symbols
if True and t and not f:
    print("true!")
else:
    print("This should never get printed")

# Chain multiple if statements together with "elif" NOT "else if"
if False or f:
    print("This should never get printed")
elif True and t and not False:
    print("This should get printed")
else:
    pass

# The "pass" statement does nothing, but it can be a filler if you want your code to run
if True:
    pass

# Python's equivalent of "switch-case" is called a "match" statement and it is more powerful
# than Java/C's switch-case. This is Python 3.10 ONLY (brand new feature!)
# match True:
#     case True:
#         print("Match case true!")
#     case False:
#         print("Match case false!")

# for loops can iterate over a range of numbers (end number is non-inclusive)
for i in range(1, 5):
    print(i)

# for loops can iterate over lists
for i in list_a:
    print(i)

# for loops can iterate over dictionaries with multiple indexing variables
# this must use .items()
for key, value in dict_a.items():
    print(f"Key: {key}, Value: {value}")

# if you are iterating over an object, you can add indexing numbers to the for loop
for index, value in enumerate(list_a):
    print(f"Index: {index}, Value: {value}")

# while loops are exactly what you might expect
i = 0
while i < 4:
    i += 1

############
# FILE I/O #
############

# Using a "with" statement as shown will keep the file open inside of the body of the
# "with" statement, and automatically close it when your code moves past the end
with open("test_file.txt", "w+") as f:
    print(f.name)
    f.write("AAAAA\n")

# This with statement is totally separate from the one above
with open("test_file.txt", "r+") as f:
    # This reads in the entire file if possible
    file_contents = f.read()

#############
# FUNCTIONS #
#############


def foo():
    # Example of a simple function definition. Notice how there is no return type, python
    # functions are void by default.
    print("A")


# Calling foo()
foo()


def bar():
    # Return types do not need to be explicitly declared. You just return whatever,
    # whenever
    return 5


x = bar()
print(x)


def foobar(a, b, c):
    # Parameters don't have types either
    return a + b + c


print(foobar(1, 2, 3))


def foobar2(a, b, c=3):
    # You can set default values for parameters, but the ones with default values MUST
    # come after any non-defaulted parameters. Default parameters can be ommitted
    return a + b + c


print(foobar2(1, 2))
print(foobar2(1, 2, 200))


###########################
# CLASSES AND DATACLASSES #
###########################

# Example class definition
class TestClass():

    # This is the constructor. Double underscore means private. You can pass values into
    # the constructor
    def __init__(self, value):
        self.variable = value

    # Methods are static by default in python
    def test1():
        # Can't access self.variable in here because that is instance-specific
        pass

    # You can make a method be tied to an instance of a class by passing in the instance
    # of that class ("self") as the first parameter. Has to be the first one.
    def test2(self):
        self.variable += 1
        print(self.variable)


# Practice instantiating a class. This is calling the __init__() method, but you don't need
# to pass in "self". Self gets automatically passed in as the first parameter
test_object = TestClass(5)
test_object.test2()


# While classes have variables and methods attached to them, dataclasses only have variables
@dataclass
class TestDataclass():
    test_int: int
    test_str: str
    test_float: float


test_dc = TestDataclass(1, "Hi", 3.333)
print(test_dc.test_float)
