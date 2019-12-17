#TESTING: testinggrounds.py - just another .py file to test, play around



'''
#which player is actually playing.
#Running a few Examples for how to change a player:
#itertools.cycle: used to cycle elements in a list.
#use next() to grab the next value

import itertools

player_choice = itertools.cycle([1, 2])

for i in range(10):
	print(next(player_choice))
	'''





'''
ITERATOR vs ITERABLE:
ITERATOR - a thing we can iterate over; like a 'for' loop
ITERABLE - a special object with next() method. Strings, Lists are iterable, but not iterators

import itertools

x = [1, 2, 3, 4] #only iterable
print(next(x)) #not an iterator, coz we can't do this line

for i in x:
	print(i)






import itertools

x = [1, 2, 3, 4] 
n = itertools.cycle(x) #iterator..., also iterable
print(next(n))

for i in n:
	print(n)
'''





'''
STRING: MAKE THE index/heading string DYNAMIC (some rules on strings)
game_size = 3
print("   0  1  2")

#s = " "
#for i in range(game_size):
	#s += "  "+str(i)

#print(s)

game_size = 3
print("   0  1  2")
#replace the line above with the line below in the actual code
s = "   "+"  ".join([str(i) for i in range(game_size)])
print(s)
'''




'''
#MAKE THE game_size DYNAMIC (LIST COMPREHENSION)
game_size = 3
game = []
for i in range(game_size):
	row = []
	for i in range(game_size):
		row.append(0)
	game.append(row)

print(game)


#the above pice of code could be condensed using a LIST COMPREHENSION, as shown below:
game_size = input("please enter the size you would like to play: ")
game = [[0 for i in range(game_size)] for i in range(game_size)]
print(game)

'''










'''
#DICTIONARIES: just a way to have KEYS and VALUES

dictionaries = {"key1":15, "key2":32}
print(dictionaries["key1"])
#set new values or add values
dictionaries["hi there"] = 92
print(dictionaries)
'''




'''
#PACKAGES, LIBRARIES, and IMPORT:

from examplemod import do_a_thing, do_another_thing

do_a_thing()
do_another_thing()

#alternative way of writing the above script
#from examplemod import do_a_thing as dat
#dat()

#NOTE: import * -- is used to import everything, just like a wild card/reg expr. Apparently not suggested.

'''



'''
#PACKAGE: Importing PACKAGES (a cluster/group of scripts). i.e., a group of scripts inside of a directory.
#MODULE: a file consisting python code (functions, classes, variables).
from moddir.examplemod import do_a_thing

do_a_thing()
'''




#PACKAGES: colorama
#when you change colors, make sure you change them back. (or everthing that comes after that will be colored by default).
#add init() method to the colorama script as shown below

from colorama import Fore, Back, Style, init
init()
print(Fore.RED + 'some red text')
print(Back.GREEN + 'and with a green background')
print(Style.DIM + 'and in dim text')
print(Style.RESET_ALL)
print('back to normal now')

