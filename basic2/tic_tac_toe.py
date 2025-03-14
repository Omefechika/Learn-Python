# using the tic tac toe game to learn python3 programming language
# game is a list of 3-lists
game = [[0, 0, 0,],
        [0, 0, 0,],
        [0, 0, 0,]]
topBar = [0, 1, 2]
sideBar = ['A', 'B', 'C']

# display column id
print("        ", end="") # this helps with design
for top in topBar:
    print(top, sep="\t", end="\t")

print()
counter = 0; # holds the current list index

#display row id and board
for side in sideBar:
    # for each entry in the sidebar list
    print(side, end="\t") # print current index value
    for row in game[counter]: # for each sublist in the game list
        print(row, sep=" ", end="\t") # display the current value
    print() # newline
    counter = counter + 1 # increament list index value
    

