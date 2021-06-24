print('today is a good day to be icecube')
print('python is cool')
print('we can even include "quotes" in strings')
print('hi' + ' world')

greeting = 'hello'
name = input('please enter your name ')
print(greeting + name)

# with inputs you can assign the value on the console and it will be stored in the variables
# hashes are for comments in python

print(greeting + ' ' + name)

tabbedString = '1\t2\t3\t4\t5'
#\t adds space between the caracthers
print(tabbedString)

# triple """ some """ escape special characters
print("""The pet shop owner said "no,no, 'e 's uh... he's resting".""")

splitString = 'This string has been \nsplit over\nseveral\nlines'
#\n adds a break line when printing
print(splitString)

anotherSplitString = """This string has been
split over
several
lines"""

print(anotherSplitString)


age = 24
print(age)

print(type(greeting))
print(type(age))

# in python you can reassign the value of a variable
age = '2 years'
print(age)
print(type(age))

#python different datatypes

#numeric
#integers and floating(1.9, 7.2, 82323.3213, etc) numbers

#iterator

#sequence(also are iterators)
#mapping
#file
#class
#exception


#operators
print('here are the operators')
a = 12
b = 3

print(a * b)
print(a - b)
print(a + b)
print(a / b)
print(a // b)  #integer division, rounded down towards minus inifity
print(a % b)   # 0 modulo: the remainder after integer division

#print every number in range 1-3 (1,2,3)
for i in range(1, a // b):
    print(i)

#operators precedence
print(a + b / 3 - 4 * 12)

print(a + (b / 3) - (4 * 12))

print(((a+b) / 3 - 4) * 12)

print()
