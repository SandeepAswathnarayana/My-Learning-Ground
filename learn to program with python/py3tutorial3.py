'''Part3: LISTS

game = [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]]

for row in game:
    print(row)'''




'''Part 4: ENUMERATE
As you iterate over something, enumerate() returns both the index value and the value of the thing that you're iterating over
game = [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]]

print("    a  b  c")

for count, row in enumerate(game):
    print(count, row)
    for  item in row:
        print(item)'''



'''Part 5: LISTS, INDEXES, VALUES, SLICES:
l = [1, 2, 3, 4, 5]
print(l)

l[1] = 99

print(l)'''



'''Part 6 and Part 7: FUNCTIONS, FUNCTION PARAMETERS, TYPING
def addition(x, y):
    return x+y

game = [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]]

def game_board():
print("    a  b  c")
for count, row in enumerate(game):
    print(count, row)
    for  item in row:
        print(item)

#use FUNCTION PARAMETERS to avoid repetitive use of the player's move like the first line below
game_board[0][1] = 1
game_board()

#Dynamic piping: python is dynamically typed. i.e., we don't define a variable as int or float or...
z = addition(5, " there")
print(z)'''



'''Part 8: MUTABILITY
#To explain why the game string here is immutable while defining outside the function
game = [1, 2, 3]
#check the unique id of an element in python using built-in function id()
print(id(game))

#use a 'function' whenever there is a repitition in your code, like the 3 lines code here below
#always use lowercase for variables, functions. That's the stadard in python styling
def game_board(player=0, row=0, column=0, just_display=False):
    global game
    game = "a game"
    print(id(game))
    print(game)
    
print(game) 
game_board(player=1, row=1, column=1)
print(game)
print(id(game))'''


'''
game = [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]]

#use a 'function' whenever there is a repitition in your code, like the 3 lines code here below
#always use lowercase for variables, functions. That's the stadard in python styling
def game_board(game_map, player=0, row=0, column=0, just_display=False):
    print("   a  b  c ")
    if not just_display:
        #logic for marking up game_board. i.e., whaever the value is passed through the parameters is whta the player has passed.
        game_map[row][column] = player
    for count, row in enumerate(game_map):
        print(count, row)
    return game_map

#running the function
game = game_board(game, just_display=True)
game = game_board(game, player=1, row=2, column=1)'''



'''Part 9: ERROR HANDLING: IndexError, Exception (general error)
game = [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]]

def game_board(game_map, player=0, row=0, column=0, just_display=False):
    
    try:
        print("   a  b  c ")
        if not just_display:
            #logic for marking up game_board. i.e., whaever the value is passed through the parameters is whta the player has passed.
            game_map[row][column] = player
        for count, row in enumerate(game_map):
            print(count, row)
        return game_map
    #add an expetion to handle Index errors 
    except IndexError as e:
        print("Error: make sure you input rows/columns as 0, 1 or 2", e)

    #add another exception (general exception) for all otehr errors
    except Exception as e:
        print("Something went wrong", e)
    #'else:' and 'finally:' are the other types of exceptions. Very rarely used though.

game = game_board(game, just_display=True)
#To explain IndexError: I am passing 'row=3' as shown below.
#To explain Exception: I am passing 'game_board' instead of 'game' as an argument while calling the function below. 
game = game_board(game_board, player=1, row=3, column=1)'''



'''Part 10: CALCULATING HORIZONTAL WINNER (whether or not we got a winner)
game = [[1, 0, 1],
        [0, 0, 0],
        [2, 2, 0]]

def win(current_game):
    for row in game:
        print(row)
        #x.count(x[0]) == len(x) --- a simple one line code to check if all elements in a list are identical (source: stackoverflow)
        if row.count(row[0]) == len(row) and row[0] != 0:
            print("Winner")

win(game)'''




'''Part 11: VERTICAL WINNER

#this vertical winner thing never seems to work apparently. Try the iterations by changing the values for all the 3 cloumns below:
#check online or browse through sentdex's written version
game = [[2, 0, 1],
        [1, 0, 1],
        [2, 2, 1]]

for col in range(len(game)):
    check = []

for row in game:
    #the print statement below iterates over all the rows and prints the 0th (first) element in each row.
     #print(row[0]) 
     #append: to add a value to the end of a list. Here you're appending row[0] to check []
     check.append(row[col])

if check.count(check[0]) == len(check) and check[0] != 0:
            print("Winner")'''


'''Part 12: DIAGONAL WINNER

game = [[1, 0, 2],
        [1, 2, 0],
        [2, 2, 1]]


diags = []
    for col, row in enumerate(reversed(range(len(game)))):
        diags.append(game[row][col])
    if diags.count(diags[0]) == len(diags) and diags[0] != 0:
        print(f"Player {diags[0]} is the winner diagonally (/)")

    
#alternative way of writing the above 4 lines of code, using enumerate.
#for col, row in enumerate(reversed(range(len(game)))):
    #print (col, row)

#reversed(): built-in function, used to check if anti-diagonal elements are identical.

diags = []
    for ix in range(len(game)):
        diags.append(game[ix][ix])
    if diags.count(diags[0]) == len(diags) and diags[0] != 0:
        print(f"Player {diags[0]} is the winner diagonally (\\)")


#logic for two diagonal elements.
#if game[0][0] == ame[1][1] == game[2][2]:
    #print("winner")
#if game[2][0] == ame[1][1] == game[0][2]:
    #print("winner")
'''





'''Part 13: BRINGING THINGS TOGETHER;
Part 14: WRAPPING UP TIC TAC TOE'''

import itertools

from colorama import Fore, Back, Style, init
init()

def win(current_game):

    def all_same(l):
        if l.count(l[0]) == len(l) and l[0] != 0:
            return True
        else: 
            return False

    #HORIZONTAL
    for row in game:
        print(row)
        #x.count(x[0]) == len(x) --- a simple one line code to check if all elements in a list are identical (source: stackoverflow)
        if all_same(row):
            print(f"Player {row[0]} is the winner horizontally")
            return True

    #DIAGONAL
    diags = []
    for col, row in enumerate(reversed(range(len(game)))):
        diags.append(game[row][col])
    if all_same(diags):
        print(f"Player {diags[0]} is the winner diagonally (/)")
        return True

    diags = []
    for ix in range(len(game)):
        diags.append(game[ix][ix])
    if all_same(diags):
        print(f"Player {diags[0]} is the winner diagonally (\\)")
        return True

    #VERTICAL
    for col in range(len(game)):
        check = []

        for row in game:
            check.append(row[col])

        if all_same(check):
            print(f"Player {check[0]} is the winner vertically (|)")
            return True

    return False


def game_board(game_map, player=0, row=0, column=0, just_display=False):
    
    try:
        if game_map[row][column] != 0:
            print("This positon is occupied. Choose another")
            return game_map, False
        print("   "+"  ".join([str(i) for i in range(len(game_map))]))
        if not just_display:    
            game_map[row][column] = player


        for count, row in enumerate(game_map):
            colored_row = ""
            for item in row:
                if item == 0:
                    colored_row += "   "
                elif item == 1:
                    colored_row += Fore.GREEN + ' X ' + Style.RESET_ALL
                elif item == 2:
                    colored_row += Fore.YELLOW + ' O ' + Style.RESET_ALL
            print(count, colored_row)


        return game_map, True
    
    except IndexError as e:
        print("Error: make sure you input rows/columns as 0, 1 or 2", e)
        return game_map, False

    except Exception as e:
        print("Something went wrong", e)
        return game_map, False

play = True
players = [1, 2]
while play:

    game_size = int(input("please enter the size you would like to play: "))
    game = [[0 for i in range(game_size)] for i in range(game_size)]

    game_won = False
    game, _ = game_board(game, just_display = True)
    player_choice = itertools.cycle([1, 2])
    while not game_won:
        current_player = next(player_choice)
        print(f"current player: {current_player}")
        played = False

        while not played:
            column_choice = int(input("what column do you want to play? (0, 1, 2): "))
            row_choice = int(input("what row do you want to play? (0, 1, 2): "))
            game, played = game_board(game, current_player, row_choice, column_choice)
            

        if win(game):
            game_won = True
            again = input("The game is over. Would you like to play again? (y/n)")
            if again.lower() == "y":
                print("restarting")
            elif again.lower() == "n":
                print("bye")
                play = False
            else:
                print("not a valid answer")
                play = False


win(game)




'''Part 14: WRAPPING UP TIC TAC TOE'''


