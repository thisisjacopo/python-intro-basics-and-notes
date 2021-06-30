#STRINGS

parrot = 'norwegian blue'

print(parrot)

#SLICE METHOD

#prints the letters of the string starting at 0
print(parrot[3], parrot[4], parrot[9], parrot[3], parrot[6], parrot[8])
#prints the letters of the string starting from the last one
print(parrot[-1])
#slice letter from 0 to 6 (6 is not included!), norweg
print(parrot[0:6])
#also, if not included the default start is position 0
print(parrot[:9])
#also, if not included the default finish is the last letter
print(parrot[10:])
#print caracthers from 0 to 6 (not included) in steps of 2
print(parrot[0:6:2]) #Nre
#print caracthers from 0 to 6 (not included) in steps of 3
print(parrot[0:6:3]) #Nw
#slices all the comas and characthers
number = '9,223;372:036 854,775;807'
separators = number[1::4]
print(separators)

values = "".join(char if char not in separators else " " for char in number).split()
print([int(val) for val in values])

#Slicing backwards

letters = 'abcdefghijklmnopqrstvwxyz'
backwards = letters[25:0:-1]
print(backwards)
backwards2 = letters[25::-1]
print(backwards2)

print(letters[16:13:-1]) #qpo
print(letters[4::-1]) #edcba
print(letters[:-9:-1]) #zyxwvtsr

#print(something[::-1]) is known as REVERSING THE SEQUENCE

