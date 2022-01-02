import os
import time
import random
from classes import *

#This is a very early development build for a world map feature.
#Not yet implemented!

#Global variables
MAP_WIDTH = 40
MAP_HEIGHT = 40
DEFAULT_WEIGHT = 10     #A common weight total
WEIGHT_INTENSITY = 5    #Higher the number, the more focused the map will be
RANDOM_INTENSITY = 20   #Higher the number, the more chaotic the map will be
INSTANTLY_GENERATE = False
AUTOMATED = False

#Map Icons
WATER = '~'
RIVER = '|'
MOUNTAIN = 'M'
PLAINS = '#'
FOREST = '^'
FIEF = 'X'
STRONGHOLD = 'H'
EMPTY = ' '
UNEXPLORED = '0'
RANDOM = '*'

#Map Icon Color
IC_WATER = textColor.BLUE
IC_RIVER = textColor.BLUE
IC_MOUNTAIN = textColor.DARK_GRAY
IC_PLAINS = textColor.YELLOW
IC_FOREST = textColor.GREEN
IC_FIEF = textColor.RED
IC_STRONGHOLD = textColor.BOLD
IC_UNEXPLORED = textColor.WARNING

#This is the primary function for generating a world map
#Utilizes a passed 'seed' value that alters how the map is generated
#The algorithm for generating the map should do the following:
#   1. Begin at a coordinate within a 2D-array
#   2. Write a character on the map
#   3. Move to new location based on current location
#   4. Determine a character to write based on adjacent locations
#   5. Loop through steps 2-4 until map is filled (unique cases aside)
#To make the starting location not matter, the algorithm should scan
#all adjacent areas to the current coordinate before deciding on a char
#to write. If no char can be found, the algo should IDEALLY pick a random location
#and try again. If it comes down to it, a manual scan from coordinate [0,0] onward
#should be performed so no spaces are left unmarked. Additionally, this adjacency 
#check should also check diagonal coordinates so that corners are not bottle-necked
#and ignored. That should increase speed and efficiency.
#
#Fief locations will be determined later, but I'd like to have something that detects
#the name of the fief and picks a location if it, say, has "Forest" in the name. More
#on that later.
def GenerateWorldMap(seed):
    os.system('clear')
    global AUTOMATED
    global INSTANTLY_GENERATE
    INSTANTLY_GENERATE = False
    AUTOMATED = False
    #worldMap = [['0'] * MAP_WIDTH] * MAP_HEIGHT    #Change this later if we want to do small/medium/large map presets
    worldMap = [['0' for x in range(MAP_WIDTH)] for y in range(MAP_HEIGHT)]

    seed = '00555' #ToDo: Make seed generator work
    sPosX = int(seed[0])
    sPosY = int(seed[1])
    freqMountain = int(seed[2])
    freqPlains = int(seed[3])
    freqForest = int(seed[4])

    symbol = FIEF
    
    loop = True
    firstLoop = True
    print('This is a test for the world map feature!')
    print('worldMap before inserting anything: \n')
    print(worldMap)
    print('\n')
    print('Inserting stuff into worldMap: \n')
    #This algorithm may be improvable. Has time-complexity O(n^2)!
    while (loop):                                   #This should keep going until the map is filled
        if firstLoop:                               #First check if this is the first loop
#            for y in range(len(worldMap[sPosY:])):          #This iterates through the height of the map from sPosY [I think]
#                for x in range(len(worldMap[y[sPosX:]])):   #This iterates through the width of the map from sPosX [I think]
#                    worldMap[x][y] = 'X'
#            for y in range(len(worldMap)):
#                for x in range(len(worldMap[y])):
#                    worldMap[x][y] = 'X'
            for y in range(MAP_HEIGHT):
                #print('Pos y: ' + str(y))
                for x in range(MAP_WIDTH):
                    #print('Pos x: ' + str(x))
               
                    temp = PrintSurroundings(worldMap, symbol, x, y, freqMountain, freqPlains, freqForest)
                    symbol = temp

                    worldMap[y][x] = symbol
            firstLoop = False
        loop = False

    print('Attempting to print world map below! \n')
#    for y in range(len(worldMap)):
#        for x in range(len(worldMap[y])):
#            print(worldMap[y][x])
#        print('\n')

#Prints out the map in a nicely spaced grid
    PrintColorMap(worldMap)
    print('\nFinished!\n')
                    
      
#Iterates through the map given the map itself and a set of 
#values to determine what to write in the next position.
#ToDo I don't think symb is actually necessary, as it is just the last
#thing drawn... which should be in the surrounding area.
#This function could likely benefit from reaching two spaces out instead of just 1, but
#that would make it far more complex. 
def PrintSurroundings(wMap, symb, posX, posY, freqM, freqP, freqF):
    global AUTOMATED
    global INSTANTLY_GENERATE
    #Create points that are surrounding our current pos
    os.system("clear")
    print('posX: ' + str(posX) + ' posY: ' + str(posY))
    try:
        print('Current symbol: ' + symb)
    except:
        print('Current symbol: None')
    try:
        dN = wMap[posY - 1][posX]
        print('There is a ' + dN + ' to the north!')
    except:
        dN = ' '
        print('North is off the map!')
    try:
        dNE = wMap[posY - 1][posX + 1]
        print('There is a ' + dNE + ' to the northeast!')
    except:
        dNE = ' '
        print('Northeast is off the map!')
    try:
        dE = wMap[posY][posX + 1]
        print('There is a ' + dE + ' to the east!')
    except:
        dE = ' '
        print('East is off the map!')
    try:
        dSE = wMap[posY + 1][posX + 1]
        print('There is a ' + dSE + ' to the southeast!')
    except:
        dSE = ' '
        print('Southeast is off the map!')
    try:
        dS = wMap[posY + 1][posX]
        print('There is a ' + dS + ' to the south!')
    except:
        dS = ' '
        print('South is off the map!')
    try:
        dSW = wMap[posY + 1][posX - 1]
        print('There is a ' + dSW + ' to the southwest!')
    except:
        dSW = ' '
        print('Southwest is off the map!')
    try:
        dW = wMap[posY][posX - 1]
        print('There is a ' + dW + ' to the west!')
    except:
        dW = ' '
        print('West is off the map!')
    try:
        dNW = wMap[posY - 1][posX - 1]
        print('There is a ' + dNW + ' to the northwest!')
    except:
        dNW = ' '
        print('North is off the map!')

    #Define a list using the surrounding symbols:
    surroundings = [dN, dNE, dE, dSE, dS, dSW, dW, dNW]
    
    print('Surroundings: ') 
    print(*surroundings)
    #Define a list of weight totals for each:
    weights = [0, 0, 0, 0, 0, 0, 0, 0]
    index = 0

    #Calculate the weight totals:
    for i in surroundings:
        if i == UNEXPLORED:
            weights[index] = 0
        elif i == EMPTY:
            weights[index] = 0
        elif i == WATER:
            weights[index] = 10
        elif i == RIVER:
            weights[index] = 10
        elif i == FOREST:
            weights[index] = freqF * WEIGHT_INTENSITY
        elif i == PLAINS:
            weights[index] = freqP * WEIGHT_INTENSITY
        elif i == MOUNTAIN:
            weights[index] =  freqM * WEIGHT_INTENSITY
        elif i == FIEF:
            weights[index] = 0
        elif i == STRONGHOLD:
            weights[index] = 0
        index = index + 1

    print('Weights: ') 
    print(*weights)
    #Define a combined list of symbols and weights:
    symbolTable = [(dN,weights[0]),(dNE,weights[1]),(dE,weights[2]),(dSE,weights[3]),(dS,weights[4]),(dSW,weights[5]),(dW,weights[6]),(dNW,weights[7]), (RANDOM,RANDOM_INTENSITY)]
    print('Symbol Table: ') 
    print(*symbolTable)
    pointTable = []
    for item, weight in symbolTable:
        pointTable.extend([item]*weight)
    newPoint = random.choice(pointTable)
    print('New Point: ') 
    print(*newPoint)
    if newPoint == RANDOM:
        newPoint = GetRandomPoint()

    if not INSTANTLY_GENERATE:
        GeneratePrintMap(wMap, posX, posY)
    
    if not AUTOMATED:
        userInput=input('Continue with manual input: press enter or input (n)')

        if userInput == 'n':
            AUTOMATED = True
            if not INSTANTLY_GENERATE:
                userInput=input('Would you like to instantly generate this map? (y/n)')
                if userInput == 'y':
                    INSTANTLY_GENERATE = True

    return newPoint

def GetRandomPoint():
    symbolTable = [(WATER, DEFAULT_WEIGHT),(FOREST, DEFAULT_WEIGHT), (PLAINS, DEFAULT_WEIGHT), (MOUNTAIN, DEFAULT_WEIGHT)]
    pointTable = []
    for item, weight in symbolTable:
        pointTable.extend([item]*weight)
    return random.choice(pointTable)

def GeneratePrintMap(wMap, posX, posY):
    for i in range(MAP_HEIGHT):
        for j in range(MAP_WIDTH):
            if i == posY and j == posX:
                print(textColor.CYAN + wMap[i][j] + textColor.RESET, end=" ")
            else:
                print(wMap[i][j], end=" ")
        print('')
    time.sleep(0.1)

def PrintColorMap(wMap):
    for i in range(MAP_HEIGHT):
        for j in range(MAP_WIDTH):
            symbol = wMap[i][j]
            if symbol == UNEXPLORED:
                print(IC_UNEXPLORED + symbol + textColor.RESET, end=" ")
            elif symbol == EMPTY:
                print(symbol, end=" ")
            elif symbol == WATER:
                print(IC_WATER + symbol + textColor.RESET, end=" ")
            elif symbol == RIVER:
                print(IC_RIVER + symbol + textColor.RESET, end=" ")
            elif symbol == FOREST:
                print(IC_FOREST + symbol + textColor.RESET, end=" ")
            elif symbol == PLAINS:
                print(IC_PLAINS + symbol + textColor.RESET, end=" ")
            elif symbol == MOUNTAIN:
                print(IC_MOUNTAIN + symbol + textColor.RESET, end=" ")
            elif symbol == FIEF:
                print(IC_FIEF + symbol + textColor.RESET, end=" ")
            elif symbol == STRONGHOLD:
                print(IC_STRONGHOLD + symbol + textColor.RESET, end=" ")
        print('')

#To Do: Write this function
def GenerateRandomSeed():
    print('\nThis does nothing!\n')

#eof