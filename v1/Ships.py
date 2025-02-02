# -+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#
# Program: Battleship - Course Project
# File: Ships.py
# Language: Python 3.7.2
#
# Description: Class for Battleship game
#
# College: Husson University
# Course: IT 262 I7-2
# Author: Célie Pierre
#
# Change Log:
# Date         Description
# --------------------------------------------------
# 2019-04-13    Initial draft
#               See BattleShip.py for more info
#
# -+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+

import random

class Game:

    def __init__(self):
        self.__emptyGrid = []
        self.__humanSG = []
        self.__humanGG = []
        self.__compSG = []
        self.__compGG = []
        self.__rowKey = []
        self.__colKey = []
        self.__shipList = []
        self.__shipDict = {}
        self.__humanScore = 0
        self.__compScore = 0
        self.__stopGame = False
        self.__winner = False


    def setEmptyGrids(self): # Empty grids
        self.__emptyGrid = [['- ','- ','- ','- ','- ','- ','- ','- ','- ','- '],
                            ['- ','- ','- ','- ','- ','- ','- ','- ','- ','- '],
                            ['- ','- ','- ','- ','- ','- ','- ','- ','- ','- '],
                            ['- ','- ','- ','- ','- ','- ','- ','- ','- ','- '],
                            ['- ','- ','- ','- ','- ','- ','- ','- ','- ','- '],
                            ['- ','- ','- ','- ','- ','- ','- ','- ','- ','- '],
                            ['- ','- ','- ','- ','- ','- ','- ','- ','- ','- '],
                            ['- ','- ','- ','- ','- ','- ','- ','- ','- ','- '],
                            ['- ','- ','- ','- ','- ','- ','- ','- ','- ','- '],
                            ['- ','- ','- ','- ','- ','- ','- ','- ','- ','- ']]
        self.__humanSG = [['- ', '- ', '- ', '- ', '- ', '- ', '- ', '- ', '- ', '- '],
                          ['- ', '- ', '- ', '- ', '- ', '- ', '- ', '- ', '- ', '- '],
                          ['- ', '- ', '- ', '- ', '- ', '- ', '- ', '- ', '- ', '- '],
                          ['- ', '- ', '- ', '- ', '- ', '- ', '- ', '- ', '- ', '- '],
                          ['- ', '- ', '- ', '- ', '- ', '- ', '- ', '- ', '- ', '- '],
                          ['- ', '- ', '- ', '- ', '- ', '- ', '- ', '- ', '- ', '- '],
                          ['- ', '- ', '- ', '- ', '- ', '- ', '- ', '- ', '- ', '- '],
                          ['- ', '- ', '- ', '- ', '- ', '- ', '- ', '- ', '- ', '- '],
                          ['- ', '- ', '- ', '- ', '- ', '- ', '- ', '- ', '- ', '- '],
                          ['- ', '- ', '- ', '- ', '- ', '- ', '- ', '- ', '- ', '- ']]
        self.__humanGG = [['- ', '- ', '- ', '- ', '- ', '- ', '- ', '- ', '- ', '- '],
                          ['- ', '- ', '- ', '- ', '- ', '- ', '- ', '- ', '- ', '- '],
                          ['- ', '- ', '- ', '- ', '- ', '- ', '- ', '- ', '- ', '- '],
                          ['- ', '- ', '- ', '- ', '- ', '- ', '- ', '- ', '- ', '- '],
                          ['- ', '- ', '- ', '- ', '- ', '- ', '- ', '- ', '- ', '- '],
                          ['- ', '- ', '- ', '- ', '- ', '- ', '- ', '- ', '- ', '- '],
                          ['- ', '- ', '- ', '- ', '- ', '- ', '- ', '- ', '- ', '- '],
                          ['- ', '- ', '- ', '- ', '- ', '- ', '- ', '- ', '- ', '- '],
                          ['- ', '- ', '- ', '- ', '- ', '- ', '- ', '- ', '- ', '- '],
                          ['- ', '- ', '- ', '- ', '- ', '- ', '- ', '- ', '- ', '- ']]
        self.__compSG = [['- ', '- ', '- ', '- ', '- ', '- ', '- ', '- ', '- ', '- '],
                         ['- ', '- ', '- ', '- ', '- ', '- ', '- ', '- ', '- ', '- '],
                         ['- ', '- ', '- ', '- ', '- ', '- ', '- ', '- ', '- ', '- '],
                         ['- ', '- ', '- ', '- ', '- ', '- ', '- ', '- ', '- ', '- '],
                         ['- ', '- ', '- ', '- ', '- ', '- ', '- ', '- ', '- ', '- '],
                         ['- ', '- ', '- ', '- ', '- ', '- ', '- ', '- ', '- ', '- '],
                         ['- ', '- ', '- ', '- ', '- ', '- ', '- ', '- ', '- ', '- '],
                         ['- ', '- ', '- ', '- ', '- ', '- ', '- ', '- ', '- ', '- '],
                         ['- ', '- ', '- ', '- ', '- ', '- ', '- ', '- ', '- ', '- '],
                         ['- ', '- ', '- ', '- ', '- ', '- ', '- ', '- ', '- ', '- ']]
        self.__compGG = [['- ', '- ', '- ', '- ', '- ', '- ', '- ', '- ', '- ', '- '],
                         ['- ', '- ', '- ', '- ', '- ', '- ', '- ', '- ', '- ', '- '],
                         ['- ', '- ', '- ', '- ', '- ', '- ', '- ', '- ', '- ', '- '],
                         ['- ', '- ', '- ', '- ', '- ', '- ', '- ', '- ', '- ', '- '],
                         ['- ', '- ', '- ', '- ', '- ', '- ', '- ', '- ', '- ', '- '],
                         ['- ', '- ', '- ', '- ', '- ', '- ', '- ', '- ', '- ', '- '],
                         ['- ', '- ', '- ', '- ', '- ', '- ', '- ', '- ', '- ', '- '],
                         ['- ', '- ', '- ', '- ', '- ', '- ', '- ', '- ', '- ', '- '],
                         ['- ', '- ', '- ', '- ', '- ', '- ', '- ', '- ', '- ', '- '],
                         ['- ', '- ', '- ', '- ', '- ', '- ', '- ', '- ', '- ', '- ']]
    def getEmptyGrids(self):
        return self.__emptyGrid, self.__humanSG, self.__humanGG, self.__compSG, self.__compGG

    def setHumanSG(self, humanSG): # Human ship grid
        self.__humanSG = humanSG
    def getHumanSG(self):
        return self.__humanSG

    def setHumanGG(self, humanGG): # Human guess grid
        self.__humanGG = humanGG
    def getHumanGG(self):
        return self.__humanGG

    def setCompSG(self, compSG): # Computer's ship grid
        self.__compSG = compSG
    def getCompSG(self):
        return self.__compSG

    def setCompGG(self, compGG): # Computer's guess grid
        self.__compGG = compGG
    def getCompGG(self):
        return self.__compGG

    def setColKey(self):
        self.__colKey = ['A','B','C','D','E','F','G','H','I','J']
    def getColKey(self):
        return self.__colKey

    def setShipDict(self):
        self.__shipDict = {'CA':['Carrier', 5, 0, 0], 'BA':['Battleship', 4, 0, 0],
                           'CR':['Cruiser', 3, 0, 0], 'SU':['Submarine', 3, 0, 0],
                           'DE':['Destroyer', 2, 0, 0]}
    def getShipDict(self):
        return self.__shipDict

    def setShipList(self):
        self.__shipList = [['Carrier', 5, 'CA', 0], ['Battleship', 4, 'BA', 0], \
                           ['Cruiser', 3, 'CR', 0], ['Submarine', 3, 'SU', 0], \
                           ['Destroyer', 2, 'DE', 0]]
    def getShipList(self):
        return self.__shipList

    def setHumanScore(self, humanScore):
        self.__humanScore = humanScore
    def getHumanScore(self):
        return self.__humanScore

    def setCompScore(self, compScore):
        self.__compScore = compScore
    def getCompScore(self):
        return self.__compScore

    def setStopGame(self, stopGame):
        self.__stopGame = stopGame
    def getStopGame(self):
        return self.__stopGame

    def setWinner(self, winner):
        self.__winner = winner
    def getWinner(self):
        return self.__winner

    def setupHumanSG(self):
        ship = 0
        while ship < len(self.__shipList):
            try:
                print('\nCurrently placing: ', self.__shipList[ship][0],
                      ' (length: ', self.__shipList[ship][1], ')', sep='')
                shipStart = input('Enter a starting point: ')
                vh = input('Place vertically (v) or horizontally (h): ')
                for c in self.__colKey:  # Find the column
                    if shipStart[0].upper().strip() == c:
                        placeCol = self.__colKey.index(c)
                placeRow = int(shipStart[1:]) - 1  # Find the row

                if self.valPlace(self.__humanSG, ship, placeCol, placeRow, vh) == True:
                    self.placeShip(self.__humanSG, ship, placeCol, placeRow, vh)
                    ship += 1
                    print('')
                    self.__str__()
                else:
                    print('\nERROR: Invalid selection. Please try again.'
                          '\n Tip: Ship cannot intersect with another ship. '
                          '\n Tip: Ship must be entirely on the board.'
                          '\n Tip: Use format A1.')
            except Exception as error:
                print('ERROR:', error,
                      ' Please enter valid input. Tip: Use format A1.')

        print('\nHuman ships have been successfully set up.')

    def setupCompSG(self):
        print('\nSetting up computer ships...')
        try:
            ship = 0
            while ship < len(self.__shipList):
                vh = random.randint(1, 2)
                if vh == 1:
                    vh = 'v'
                else:
                    vh = 'h'
                placeRow = random.randint(1, 10)
                placeCol = random.randint(1, 10)
                if self.valPlace(self.__compSG, ship, placeCol, placeRow, vh) == True:
                    self.placeShip(self.__compSG, ship, placeCol, placeRow, vh)
                    ship += 1
            # self.compDisplay() # FOR TESTING ONLY
            print('Computer ships have been successfully set up.')
        except Exception as error:
            print('ERROR in Game.setupCompSG:\nError details:', error)

    def compDisplay(self): # FOR TESTING ONLY
        # Display the comp's ship and guess grids
        print('               COMP SHIP GRID')
        print('---------------------------------------------')
        print('     A   B   C   D   E   F   G   H   I   J')
        for hsRow in range(len(self.__compSG)):
            if hsRow < 9:
                rowDisplay = ' ' + str(hsRow + 1) + ' '
            elif hsRow >= 9:
                rowDisplay = str(hsRow + 1) + ' '
            for hsCol in range(len(self.__compSG)):
                rowDisplay = rowDisplay + '  ' + str(self.__compSG[hsRow][hsCol])
            print(rowDisplay)


    def placeShip(self, shipGrid, ship, placeCol, placeRow, vh):
        try:
            if vh.lower().strip() == 'v':  # Place ship vertically
                stop = placeRow + self.__shipList[ship][1]
                while placeRow < stop and shipGrid[placeRow][placeCol] == '- ':
                    shipGrid[placeRow][placeCol] = self.__shipList[ship][2]
                    placeRow += 1
            elif vh.lower().strip() == 'h':  # Place ship horizontally
                stop = placeCol + self.__shipList[ship][1]
                while placeCol < stop and shipGrid[placeRow][placeCol] == '- ':
                    shipGrid[placeRow][placeCol] = self.__shipList[ship][2]
                    placeCol += 1
            return shipGrid
        except Exception as error:
            print('ERROR in Game.placeShip:\nError details:', error)


    def valPlace(self, shipGrid, ship, placeCol, placeRow, vh):
        try:
            if vh.lower().strip() == 'v':  # Vertical placement
                stop = placeRow + self.__shipList[ship][1]
                while placeRow < stop:
                    if shipGrid[placeRow][placeCol] == '- ':
                        placeRow += 1
                    else:
                        return False
                return True
            elif vh.lower().strip() == 'h':  # Horizontal placement
                stop = placeCol + self.__shipList[ship][1]
                while placeCol < stop:
                    if shipGrid[placeRow][placeCol] == '- ':
                        placeCol += 1
                    else:
                        return False
                return True
        except:
            return False


    def __str__(self):
        # Display the user's ship and guess grids
        print('               HUMAN SHIP GRID                                 HUMAN GUESS GRID')
        print('-----------------------------------------------------------------------------------------------')
        print('     A   B   C   D   E   F   G   H   I   J           A   B   C   D   E   F   G   H   I   J')
        for hsRow in range(len(self.__humanSG)):
            if hsRow < 9:
                rowDisplay = ' ' + str(hsRow + 1) + ' '
            elif hsRow >= 9:
                rowDisplay = str(hsRow + 1) + ' '
            for hsCol in range(len(self.__humanSG)):
                rowDisplay = rowDisplay + '  ' + str(self.__humanSG[hsRow][hsCol])
            if hsRow < 9:
                rowDisplay = rowDisplay + '      ' + str(hsRow + 1) + ' '
            elif hsRow >= 9:
                rowDisplay = rowDisplay + '     ' + str(hsRow + 1) + ' '
            for hgCol in range(len(self.__humanGG)):
                rowDisplay = rowDisplay + '  ' + str(self.__humanGG[hsRow][hgCol])
            print(rowDisplay)


    def turnUser(self): # Human's turn
        print()
        self.__str__()
        print('    (X = Save & Exit)')
        print('\nHuman\'s turn.')
        validShot = False
        while not validShot:
            try:
                userShot = input('Human! Fire!: ')
                if userShot.lower().strip() == 'x': # Exit option
                    self.setStopGame(True)
                    validShot = True
                else: # Keep playing
                    for c in self.getColKey(): # Find the column
                        if userShot[0].upper() == c:
                            shotCol = self.getColKey().index(c)
                    shotRow = int(userShot[1:]) - 1 # Find the row
                    validShot = self.turn('human', self.__compSG, self.__humanGG, shotRow, shotCol)
            except Exception as error:
                print('ERROR: Please enter a valid shot.\n'
                      'Error in Game.turnUser; Error details:', error)
                validShot = False


    def turnComp(self): # Computer's turn
        try:
            print('\nComputer\'s turn.')
            validShot = False
            while not validShot:
                shotCol = random.randint(0, 9)
                shotRow = random.randint(0, 9)
                validShot = self.turn('comp', self.__humanSG, self.__compGG, shotRow, shotCol)
        except Exception as error:
            print('ERROR in Game.turnComp:\nError details:', error)


    def turn(self, player, opponentSG, playerGG, shotRow, shotCol):
        try:
            shot = opponentSG[shotRow][shotCol]
            if shot == '- ': # Miss
                opponentSG[shotRow][shotCol] = 'M '
                playerGG[shotRow][shotCol] = 'M '
                print('  MISS!')
                return True
            elif shot in self.__shipDict: # Hit
                print('  HIT! You hit the ', self.__shipDict.get(shot)[0], '!', sep='')
                opponentSG[shotRow][shotCol] = 'H '
                playerGG[shotRow][shotCol] = 'H '
                if player == 'human':
                    self.__shipDict.get(shot)[2] += 1
                    if self.__shipDict.get(shot)[2] == self.__shipDict.get(shot)[1]:
                        print('  SCORE! The ', self.__shipDict.get(shot)[0], ' has sunk!', sep='')
                        self.__humanScore += 1
                elif player== 'comp':
                    self.__shipDict.get(shot)[3] += 1
                    if self.__shipDict.get(shot)[3] == self.__shipDict.get(shot)[1]:
                        print('  SCORE! The ', self.__shipDict.get(shot)[0], ' has sunk!', sep='')
                        self.__compScore += 1
                return True
            elif shot == 'M ' or shot == 'H ' :
                print('ERROR! You\'ve already shot here. Please try again.')
                return False
            else:
                print('ERROR: Please enter a valid shot.')
                return False
        except Exception as error:
            print('ERROR in Game.turn:\nError details:', error)


    def score(self):
        try:
            if self.__humanScore < len(self.__shipList) and \
               self.__compScore < len(self.__shipList):
                print('\nCurrent Score: '
                      '\n  Human:    ', self.__humanScore,
                      '\n  Computer: ', self.__compScore)
            else:
                print()
                print(' _       ___\n'
                      '| |     / (_)___  ____  ___  _____\n'
                      '| | /| / / / __ \/ __ \/ _ \/ ___/\n'
                      '| |/ |/ / / / / / / / /  __/ /\n'
                      '|__/|__/_/_/ /_/_/ /_/\___/_/')
                if self.__humanScore == len(self.__shipList):
                    print('    __  ____  ____  ______    _   ____\n'
                          '   / / / / / / /  |/  /   |  / | / / /\n'
                          '  / /_/ / / / / /|_/ / /| | /  |/ / /\n'
                          ' / __  / /_/ / /  / / ___ |/ /|  /_/\n'
                          '/_/ /_/\____/_/  /_/_/  |_/_/ |_(_)')
                elif self.__compScore == len(self.__shipList):
                    print('   __________  __  _______  __  __________________  __\n'
                          '  / ____/ __ \/  |/  / __ \/ / / /_  __/ ____/ __ \/ /\n'
                          ' / /   / / / / /|_/ / /_/ / / / / / / / __/ / /_/ / /\n'
                          '/ /___/ /_/ / /  / / ____/ /_/ / / / / /___/ _, _/_/\n'
                          '\____/\____/_/  /_/_/    \____/ /_/ /_____/_/ |_(_)')
                print('\nFinal Score: '
                  '\n  Human:    ', self.__humanScore,
                  '\n  Computer: ', self.__compScore)
                self.setWinner(True)
        except Exception as error:
            print('ERROR in Game.score:\nError details:', error)
