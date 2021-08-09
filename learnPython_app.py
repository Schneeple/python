#!/usr/bin/python

print('hello world')

print('this has begun')

x=input('what is the valuye of x:')
def func(x):
	if x== 1:
		print('mofo')
	elif x== 2:
		print('mofo 2')
	elif x == 3:
		print('mofo 3')
	else:
		print('youre a liar, your mom is a hoe')
you_mom= func(x)


try:
	num1=5363
	num2=0
	print(num1/num2)
	print('done')		
except:
	print('love your titties')
	
try:
	print('Hello')
	print(1/0)
except ZeroDivisionError:
	print('Divided by zero Error!')
	
finally:
	print('line 34')

print('raise module:')
num = input('input number:')
if float(num)< 0:
	raise ValueError("Negative")

#how the fuck does a raise work??
#jk i think i figured it out

#Assertion... programmers place these at the start of a function 
#to check for valid input, and after the function call to chek for valid output

print('Assertion module:')
# Question: What is the highest number that is displayed???
print(0)
assert "h"!= "w"
print(1)


x=input("What is x?:")
def my_func(x):
	assert x>0, "Error!"
print(x)
my_func(x)


print("How to open a file:")

print('myfile=open("filename.txt")')
print('myfile=open("filename.txt","w")  is to open the file to read')
print('myfile=open("filename.txt","w")  is to open the file to write')
print('myfile=open("filename.txt","a")  is to open the file to append')
print('myfile=open("filename.txt","wb")  is to open the file to binary mode')

print('To close a file use the file.close() command')

print('cont=file.read() will print all the content in the file')
print('if you want a certain amount of bytes read use file.read(#_of_bytes)')

# This code teaches you how to open a text file and read each line.
file = open("text.txt", "r")
for line in file:
	print(line)
file.close()


# This code teaches you hopw to write a line into a newfile or existing one
file=open("newfile.txt","w")
file.write("hello you communist fuck, I have just added this to the file!!!!")
file.close()

# Demonstration of how writing and reading files start to work together.
file = open("newfile.txt","r")
print("Reading initial contents")
print(file.read())
print("Finished")
file.close()

file=open("newfile.txt","w")
file.write('new input')
file.close()

file = open("newfile.txt", "r")
print("Reading new content")
print(file.read())
print("Finished reading new content")
file.close()

# Note: if you open a file in write mode the contents will be deleted...
# Write method will return the number of bytes

msg = "Hello World"
print(msg)
file = open("newfile.txt", "w")
amount_written = file.write(msg)
print(amount_written)
file.close()

print(len(msg))
## You have got to figure out why [file.write(msg) != len (msg)]

# To avoid wasting resources, you can close files this way!

#try:
#	f=open("newfile.txt.")
#	print(f.read())
#finally:
#	f.close()

with open("text.txt") as f:
	print(f.read())

## New MODULE_______________________________________________________ [ More Types ]


#Example of None / null functions! 
#def some_func():
#	print('Hello Roberto')
#var = some_func()
#print(var)
#some_func()

# Example of dictionaries
ages={ 'Dave': 24, 'Mary': 12, 'Josh': 22}

print(ages['Mary'])
	
print(ages['Dave'])

# Key errors
primary= {
	"red":[255,0,0,],
	"green" :[0,255,0],
	"blue": [0,0,255]
	}
	
# print(primary["red"])
# print(primary["yellow"])
	
# immutable dictionaries cause a TypeError; this occurs 

# because you have to define the words to the letters.

bad_dict={
#   [1,2,3]: "one two three",
}
# What will it print? ANS: 17
# primes={ 1:2, 2:3 , 4:7 , 7:17}
# print(primes[primes[4]])



# Tuples are the same as lists but are immutable.
# immutable
# tuples can be spliced
words = ("spam", "eggs", "cheese")
print words[0]

# Trying to assign a variable to a tuple will give a TypeError:
# EX:    words[1]="ass"   cannot be done, will cause error.

# List
# list=[1,2]
# 
# Dictionary
# dict={1:"one",2:"two"}
# 
# Tuples
# tuple=("one","two")

my_tupl = "one","two","three"
print(my_tupl[0])

print "empty tuples can not be changed,  but are faster than lists using...tupl=()"

tupl=()
print(tupl)

# List slices.......provide a more advanced way of retrieving values from a list

squares= [0,1,2,4,9,16,25,36,49,64,81]
print(squares[2:6])
print squares[1:4]
print squares[0:1]
# NOTE: Last digit is not displayed!!!!

print(squares[:7]) # : before will print everything before 7...
print(squares[7:]) # : after will print everything after 7...
print(squares[2:8:3]) # will produce a step size( the third number)
print(squares[::2]) # Will print every 2 numbers

print squares[1::-1] # negative can be used for slicing, and will work backwards...
# negative values in the first or second number [#,#,x] it will work from end of row.


# What will be the output of this code?? ANS: [1,16,64]
print squares[1::4]
# What will be the output of this code?? ANS: [36,25]
print squares[7:5:-1]

# List comprehensions... a way to quickly create lists whose contents obey a rule.
cubes = [i**3 for i in range(5)]
print cubes

#1.  What does this list do?? ANS: a list of even numbers between 0 and 18
nums= [i*2 for i in range(10)]
print nums

# can also make conditions on these like so..
evens = [i**2 for i in range(10) if i**2 % 2 ==0]
print evens
# NOTE: it will print the squares that have no remainder when divided by two (even #'s)

# creating a large list that your computer will crash will create a MemoryError.
# EX: even=[2*i for i in range(10**100)]

# String Formatting.....a powerful way to embed non-strings within strings.

nums = [4,5,6]
msg = "Numbers : {0} {1} {2}". format(nums[0], nums[1], nums[2])
print msg

# 1. What is the results of this code? ANS: abracadabra
print "{0}{1}{0}". format ("abra","cad")


a= "{x} {y}". format(x=5,y=12)
print(a)

# OML A BUNCH OF COMMANDS...
# join- joins a list of strings with a serpator
# replace- replaces one string with another
# startswith and endswith- determine if there is a string is a substring at the start/end
# lower/upper- change the case of the string.
# split/join- opposite of join, turning a string into two strings with a seperator

print(", ".join(["spam", "eggs", "ham"]))
#prints "spam, eggs, ham"

print("Hello ME".replace("ME", "world"))
#prints "Hello world"

print("This is a sentence.".startswith("This"))
# prints "True"

print("This is a sentence.".endswith("sentence."))
# prints "True"

print("This is a sentence.".upper())
# prints "THIS IS A SENTENCE."

print("AN ALL CAPS SENTENCE".lower())
#prints "an all caps sentence"

print("spam, eggs, ham".split(", "))
#prints "['spam', 'eggs', 'ham']"

# all any and enumerate functions
nums = [ 56, 34, 6, 23, 100]
if all ([i>5 for i in nums]):
	print " I got a big fat dick."
if any([i % 2 ==0 for i in nums]):
	print "i am flacid and atleast one of these numbers is even."
for v in enumerate(nums):
	print v

# Text analyzer

# filename = input("Enter a mother fucking file name:")

# with open(filename) as f:
# 	test = f.read()
# print text

def count_char(text,char):
	count = 0
	for c in text:
	 if c == char:
		count+=1
	return count
print(count_char("onimonipia","i"))

# NEW MODULE....................................................FUNCTIONAL PROGRAMMING...

def apply_twice(func,arg):
	return func(func(arg))

def add_five(x):
	return x+5
	
print(apply_twice(add_five,10))

# Pure functions.......
def pure_func(x,y):
	temp=x+2*y
	return temp/(2*x+y)
	
# Immpure functions.....
some_list=[]

def impure(arg):
	some_list.append(arg)
	
# lambda functions...........

def my_func(f,arg):
	return f(arg)
y=my_func(lambda x: 2*x*x,5)	
print y

#named function
def polynomial(x):
	return x**2 + 5*x + 4
print(polynomial(-4))

#lambda
print((lambda x: x**2 + 5*x + 4) (-4))

print (lambda x: x*x)(8)

# map and filter
def add_five(x):
	return x+5

nums =[11,22,33,44,55]
resultss=list(map(add_five,nums))
print(resultss)

nums = [ 11, 22 ,33 ,44 ,55]
res= list(filter(lambda x : x%2 == 0, nums))
print res

# Generator
def countdown():
   i=5
   while i>0:
	  yield i
	  i-=1
	
for i in countdown():
   print (i)	
   
def numies(x):
	for i in range(x):
		if i%2 ==0:
		 yield i
		 
print(list(numies(15)))
	
# Decorators - way to modify functions using other functions;'

def decor(func):
	def wrap():
		print("=======")
		func()
		print("+++++++")
	return wrap
	
def print_text():
	print("Hello World")
decorated = decor(print_text)
decorated()
	
# instead of using
def print_text():
	print("Hello World")
print_text=decor(print_text)	

# Use....

@decor
def print_text():
	print("Hello World")


# Recursion

def factorial(x):
	if x==1:
	 return 1
	else:
	  return x * factorial(x-1)
print(factorial((5)))	
	
# NOTE: need a base case or it can run forever
# Note: can also be indiriect, for ex:

def is_even(x):
	if x==0:
		return True
	else: 
		return is_odd(x-1)
def is_odd(x):
	return not is_even(x)
	
print(is_odd(17))
print(is_even(23))	

def fib(x):
	if x==0 or x == 1:
		return 1
	else:
		return fib(x-1) + fib(x-2)
print(fib(4))

# SETS



#  itertools

# from itertools import count
# 
# for i in count(3):
# 	print(i)
# 	if i >=11:
# 		break
		
# this command can also do the cycle, or repeat from the itertools libary....
# takewhile-takes items frtom an iterable while a predicate function remains true...
# chain- combines serveral iterable into one long one...
# accumulate-returns a running total of values in an iterable.

# import takewhile 
# 
# nums=[ 2, 4 , 6 , 7, 9, 8]
# 
# a = takewhile(lambda x: x%2==0, nums)

print "Module 6 Quiz"
def power(x,y):
	if y==0:
		return 1
	else:
		return x* power(x,y-1)


print power(2,3)


#  ...............................................OBJECT - ORIENTED -PROGRAMMING MODULE	
	
# ex1	
class Cat:
  def __init__(self, color, legs):
    self.color = color
    self.legs = legs

felix = Cat("ginger", 4)
rover = Cat("dog-colored", 4)
# 
# 
# try1	

# prob1
class Student:
	def __init__(self,name):
		self.name = name

test=Student("Bob")	
print(Student)

# EX of a class

class Customer(object):
    """A customer of ABC Bank with a checking account. Customers have the
    following properties:

    Attributes:
        name: A string representing the customer's name.
        balance: A float tracking the current balance of the customer's account.
    """

    def __init__(self, name,balance):
        """Return a Customer object whose name is *name*.""" 
        self.name = name
        self.balance = balance

    def withdraw(self, amount):
        """Return the balance remaining after withdrawing *amount*
        dollars."""
        if amount > self.balance:
            raise RuntimeError('Amount greater than available balance.')
        self.balance -= amount
        return self.balance

    def deposit(self, amount):
        """Return the balance remaining after depositing *amount*
        dollars."""
        self.balance += amount
        return self.balance


ass=Customer('Colton', 1000000)
print(ass.balance)


rhys_neary_balance= input( 'how much are you depositing?:')
rhys_neary	= Customer('Rhys Neary', rhys_neary_balance)
print(rhys_neary.balance)



class Cat:
  def __init__(self, color, legs):
    self.color = color
    self.legs = legs

felix = Cat("ginger", 4)
rover = Cat("dog-colored", 4)
stumpy = Cat("brown", 3)

# Inheritance

class Animal: 
  def __init__(self, name, color):
    self.name = name
    self.color = color

class Cat(Animal):
  def purr(self):
    print("Purr...")
        
class Dog(Animal):
  def bark(self):
    print("Woof!")

fido = Dog("Fido", "brown")
print(fido.color)
fido.bark()

# Both of the animals can "inherite" the same class


# Magic Methods & Operator Overloading

class Vector2D:
  def __init__(self, x, y):
    self.x = x
    self.y = y
  def __add__(self, other):
    return Vector2D(self.x + other.x, self.y + other.y)

first = Vector2D(5, 7)
second = Vector2D(3, 9)
result = first + second
print(result.x)
print(result.y)


# creation
# manipluation
# destruction
#  these are commands that can affect the object's lifecycle



# Data hiding uses one underscore in from to show that it is going to be hidden.

# use @classmethod and @ staticmethod are passed to class conductor NOT THE self method.

# use @property to customize access to instance attributes
# ex:

class Pizza:
  def __init__(self, toppings):
    self.toppings = toppings
    self._pineapple_allowed = False

  @property
  def pineapple_allowed(self):
    return self._pineapple_allowed

  @pineapple_allowed.setter
  def pineapple_allowed(self, value):
    if value:
      password = input("Enter the password: ")
      if password == "Sw0rdf1sh!":
        self._pineapple_allowed = value
      else:
        raise ValueError("Alert! Intruder!")

pizza = Pizza(["cheese", "tomato"])
print(pizza.pineapple_allowed)
pizza.pineapple_allowed = True
print(pizza.pineapple_allowed)




# A Simple game 
# Ex:

class GameObject:
  class_name = ""
  desc = ""
  objects = {}

  def __init__(self, name):
    self.name = name
    GameObject.objects[self.class_name] = self

  def get_desc(self):
    return self.class_name + "\n" + self.desc

class Goblin(GameObject):
  class_name = "goblin"
  desc = "A foul creature"

goblin = Goblin("Gobbly")

def examine(noun):
  if noun in GameObject.objects:
    return GameObject.objects[noun].get_desc()
  else:
    return "There is no {} here.".format(noun)

# We created a Goblin class, which inherits from the GameObjects class.
# We also created a new function examine, which returns the objects description.
# Now we can add a new "examine" verb to our dictionary and try it out!



# This part is added in so that you can attack and kill the goblin!

class Goblin(GameObject):
  def __init__(self, name):
    self.class_name = "goblin"
    self.health = 3
    self._desc = " A foul creature"
    super().__init__(name)

  @property
  def desc(self):
    if self.health >=3:
      return self._desc
    elif self.health == 2:
      health_line = "It has a wound on its knee."
    elif self.health == 1:
      health_line = "Its left arm has been cut off!"
    elif self.health <= 0:
      health_line = "It is dead."
    return self._desc + "\n" + health_line

  @desc.setter
  def desc(self, value):
    self._desc = value

def hit(noun):
  if noun in GameObject.objects:
    thing = GameObject.objects[noun]
    if type(thing) == Goblin:
      thing.health = thing.health - 1
      if thing.health <= 0:
        msg = "You killed the goblin!"
      else: 
        msg = "You hit the {}".format(thing.class_name)
  else:
    msg ="There is no {} here.".format(noun) 
  return msg


	
	
# Regular Expressions....................................................................

import re

pattern = r"spam"

if re.match(pattern, "spa"):
   print("Match")
else:
   print("No match")
   
   
   
#    Can also use re.search and re.findall to search for strigns

import re

pattern = r"spam"

if re.match(pattern, "eggspamsausagespam"):
   print("Match")
else:
   print("No match")

if re.search(pattern, "eggspamsausagespam"):
   print("Match")
else:
   print("No match")
    
print(re.findall(pattern, "eggspamsausagespam"))


# Metacharacters .... *,+,?,{ and } ..................................................

pattern = r"egg(spam)*"

if re.match(pattern,"egg"):
	print "Match 1"
if re.match(pattern, "eggspameggspam"):
	print "Match 2"
if re.match(pattern, "spam"):
	print "Match 3"

# the * looks for zero or more "spam"s with "egg" at the front of it

#  + is the same as * but does ONE or more repititions


#  ? means zero or one repititions

# fill in the blanks to match both 'color' and 'colour'

pattern=r"colo(u)?r"

# Curly brackets work the same as the ? but you can specify the repitions
# EX:  ?={0,1}  .......can have 2 to 3 repitions by using {2,3}

# GROUPS...........................................................................

pattern = r"a(bc)(de)(f(g)h)i"

match = re.match (pattern, "abcdefghijklmnop")
if match:
		print(match.group())
		print(match.group(0))
		print(match.group(1))
		print(match.group(2))
		print(match.group(3))
		print(match.groups())
		
		
# named groups have the format (?P<name>....)
# Non-capturing groups ahve the format (?:....)


pattern = r"(?P<first>abc)(?:def)(ghi)"

match = re.match(pattern, "abcdefghi")
if match:
	print(match.group("first"))
	print(match.groups())

# | is the sign to put in between two charcters to put "or"

# special sequences..................................................................
# they are written with a backslash and a number between 1 and 99
print "Start of special sequences section!"


pattern = r"(.+)\1"

match= re.match(pattern,"word word")
if match:
	print "match 1"
	
match= re.match(pattern, "?! ?!")
if match:
	print "Match 2"
	
match=re.match(pattern,"abc cde")
if match:
	print "Match 3"
	
	
# \d \s \w 9 digits, whitespace, and word characters are useful special sequences

# \D \S \W are if there are no digits .etc

# \A \Z match the begining and end of the string
# \b matches the empty string between \w and \W.

pattern= r"\b(cat)\b"

match = re.search(pattern, "The cat sat!")
if match:
	print "Match1"
	
match = re.search(pattern, "the dog s<cat>attered")
if match:
	print "Match2"
	
match = re.search(pattern, "the dog scattered")
if match:
	print "Match3"
	
	
	
# Email Extraction.....................................................................
import re

pattern=r"([\w\.-]+)@([\w\.-]+)(\.[\w\.]+)"
str= "Please contact info@sololearn.com for assistance."

match=re.search(pattern, str)
if match:
	print(match.group())
	

# .....................................................................Pythonicness......

# The Zen of Python...................................................................
import this

# PEP Python Enhancement Proposals....................................................

# PEP8 is a style of writing codes

# Function Arguments...................................................................

# *args enables you to pass an arbituary number of arguments to that function

def function(named_arg,*args):
	print(named_arg)
	print(args)
	
function(1,2,3,4,5)

# Defualt Values

def function(x,y,food="spam"):
	print(food)

function(1,2)
function(3,4,"egg")

# **kwargs allows you to handle named arguments that you have not defined in advance

def fuq(x,y=7,*args,**kwargs):
	print(kwargs)
	
fuq(2,3,4,5,6,a=7,b=8)



# Tuple Unpacking......................................................................

numbers = (1,2,3)
a,b,c= numbers

print a
print b
print c

# numbers = a,b,*c,d is an example of the c being a list of the rest of the list

# Ternary Operator......................................................................

a = 7
b=1 if a>=5 else 42
print(b)

# __main__........................................................................

# def function():
# 	print("This is a module function")
# 
# if__name__ == "__main__"
#  print("Hello")


# Major 3rd Party Libraries.............................................................

# CherryPy, Flask, beautiful Soup

import matplotlib
import numpy
import scipy
# import Panda3D
import pygame

# Packaging............................................................................

# puyts modules yu have qritten in a standard format, use setuptools, distutils

# for macs use py2app, PyInstaller cx_freeze















	
	
	
	
	
	
	



