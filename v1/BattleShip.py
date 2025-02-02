# -+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#
# Program: Battleship - Course Project
# File: BattleShip.py
# Language: Python 3.7.2
#
# Description: Battleship game, human vs. computer
#
# College: Husson University
# Course: IT 262 I7-2
# Author: Célie Pierre
#
# Change Log:
# --------------------------------------------------
# Date          Description
# --------------------------------------------------
# 2019-04-13    Initial draft
#               Create setGrids function
# 2019-04-20    Create Grids class, move functions
#               Add human ship placement
# 2019-04-22    Add computer ship placement
# 2019-04-27    Updated ship setup
#               Added Game subclass
# 2019-04-28    Added additional gameplay elements
#               Debugged some grid/game errors
# 2019-04-29    Fixed human guess grid display bug
# 2019-04-30    Added ASCII art
#               ASCII font: Slant by Glenn Chappell
#               Added score method
#               Error testing and bug fixes
# 2019-05-01    Lots of error testing and debugging
#               Simplified code where possible
#               Fixed randomized computer setup
# 2019-05-06    Error testing
#               Fixed bug in score keeping
#
# -+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+

import Ships
import pickle

INSTRUCT = 1
SAVED = 2
NEW = 3
EXIT = 4

def main():
    welcome()
    try:
        userChoice = menu()
        while userChoice != EXIT:
            if userChoice == INSTRUCT:
                instructions()
            elif userChoice == SAVED:
                try:
                    playGame(loadGame())
                except:
                    print('Please start a new game')
            elif userChoice == NEW:
                game = gameSetup()
                playGame(game)
            userChoice = menu()
    except Exception as error:
        print('ERROR in main():\n', error)

    print('Thanks for playing!\nGoodbye.')


def welcome():
    print('\n                       ' + '                 Welcome to')
    print('                         ' + '   ___       __  __  __    ______   _\n'    
          '                         ' + '  / _ )___ _/ /_/ /_/ /__ / __/ /  (_)__ \n'    
          '                         ' + ' / _  / _ `/ __/ __/ / -_)\ \/ _ \/ / _ \ \n'    
          '                         ' + '/____/\_,_/\__/\__/_/\__/___/_//_/_/ .__/\n'    
          '                         ' + '                                  /_/    ')
    print('                         ' + '          Let the games begin!\n')


def menu():
    print('\n   MAIN MENU'
          '\n1) Instructions'
          '\n2) Continue saved game'
          '\n3) Start new game'
          '\n4) Exit')
    try:
        userChoice = int(input('Please make a menu selection: '))
    except:
        print('ERROR: Please make a valid selection')
    return userChoice


def instructions():
    print('\nHow to play:\n')
    print(' Ship Setup'
          '\n   You will place your ships on your ship grid by selecting a '
          '\n   starting point (see formatting below).'
          '\n   Ships can be placed either vertically or horizontally.'
          '\n   Ships cannot be placed diagonally.'
          '\n   Ships cannot overlap and must be placed entirely on your ship grid.'
          '\n   The computer\'s ship grid will be automated and random.')
    print('\n Gameplay Directions'
          '\n   Your goal is to sink your opponent\'s entire fleet of ships.'
          '\n   Each opponent will take a shot then the next player will go.'
          '\n   Turns will alternate until a winner is declared.'
          '\n   If a ship is hit, the hit ship\'s name will display and the guess grid'
          '\n   will display an X.'
          '\n   If a ship is missed, the guess grid will display an M.'
          '\n   A player wins by sinking all of their opponent\'s ships.')
    print('\n Formatting'
          '\n   When placing your ship or taking a shot, use format LN (L = letter, N = number).'
          '\n   For example, A1 or C3. It is not case sensitive.')
    print('\n Exit the game'
          '\n   If at any point you\'d like to exit the game,'
          '\n   simply enter X during your turn.'
          '\n   You will have the option to save the game before exiting.'
          '\n   Ship grid must be set up in order to save a game.')


def loadGame():
    try:
        with open('savedGame.dat', 'rb') as gameFile:
            game = pickle.load(gameFile)
            print('Game has been successfully loaded.\n')
        return game
    except Exception as error:
        print('ERROR: Cannot load saved game. Please start a new game\nError details:', error)


def saveGame(game):
    saveGame = input('\nYou have chosen to exit the game.'
                     '\nWould you like to save the game before exiting (y/n)? ')
    if saveGame == 'y':
        try:
            with open('savedGame.dat','wb') as gameFile:
                gameData = game
                pickle.dump(gameData, gameFile)
                print('Current game has been successfully saved.')
        except Exception as error:
            print('ERROR in saveGame.\nError details:', error)


def gameSetup():
    print('\nLet\'s set up the ships...\n')
    try:
        ships = Ships.Game()                # Instantiate the ships object
        ships.setEmptyGrids()               # Set up
        ships.setShipDict()                 # Set the ship dictionary
        ships.setShipList()                 # Set the ship dictionary
        ships.setColKey()                   # Set the column key
        ships.__str__()                     # Display the starting ships
        print('\nHuman! Set up your Ship Grid.')
        ships.setupHumanSG()                # Human ship setup
        ships.setupCompSG()                 # Computer ship setup
        return ships
    except Exception as error:
        print('ERROR in gameSetup.\nError details:', error)


def playGame(game):
    try:
        game.setStopGame(False)
        while not game.getStopGame() and not game.getWinner():
            game.turnUser()
            game.score()
            if not game.getStopGame() and not game.getWinner():
                game.turnComp()
                game.score()
            if game.getStopGame(): # Stop and save game
                saveGame(game)
    except Exception as error:
        print('ERROR in playGame.\nError details:', error)


main()
