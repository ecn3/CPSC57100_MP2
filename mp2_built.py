""" 
Christian Nelson
9/29/2020
CPSC-57100-002, Fall 2020
Machine Problem 2: Tic-Tac-Toe
"""


import numpy as np
import random
import math

# self class is responsible for representing the game board
class GenGameBoard: 
    
    # Constructor method - initializes each position variable and the board size
    def __init__(self, boardSize):
        self.boardSize = boardSize  # Holds the size of the board
        self.marks = np.empty((boardSize, boardSize),dtype='str')  # Holds the mark for each position
        self.marks[:,:] = ' '
    
    # Prints the game board using current marks
    def printBoard(self): 
        # Prthe column numbers
        print(' ',end='')
        for j in range(self.boardSize):
            print(" "+str(j+1), end='')
        
        
        # Prthe rows with marks
        print("")
        for i in range(self.boardSize):
            # Prthe line separating the row
            print(" ",end='')
            for j in range(self.boardSize):
                print("--",end='')
            
            print("-")

            # Prthe row number
            print(i+1,end='')
            
            # Prthe marks on self row
            for j in range(self.boardSize):
                print("|"+self.marks[i][j],end='')
            
            print("|")
                
        
        # Prthe line separating the last row
        print(" ",end='')
        for j in range(self.boardSize):
            print("--",end='')
        
        print("-")
    
    
    # Attempts to make a move given the row,col and mark
    # If move cannot be made, returns False and prints a message if mark is 'X'
    # Otherwise, returns True
    def makeMove(self, row, col, mark):
        possible = False  # Variable to hold the return value
        if row==-1 and col==-1:
            return False
        
        # Change the row,col entries to array indexes
        row = row - 1
        col = col - 1
        
        if row<0 or row>=self.boardSize or col<0 or col>=self.boardSize:
            print("Not a valid row or column!")
            return False
        
        # Check row and col, and make sure space is empty
        # If empty, set the position to the mark and change possible to True
        if self.marks[row][col] == ' ':
            self.marks[row][col] = mark
            possible = True    
        
        # Prout the message to the player if the move was not possible
        if not possible and mark=='X':
            print("\nself position is already taken!")
        
        return possible
    
    
    # Determines whether a game winning condition exists
    # If so, returns True, and False otherwise
    def checkWin(self, mark): # may need to be modified or overriden by min max
        won = False # Variable holding the return value
        
        # Check wins by examining each combination of positions
        
        # Check each row
        for i in range(self.boardSize):
            won = True
            for j in range(self.boardSize):
                if self.marks[i][j]!=mark:
                    won=False
                    break        
            if won:
                break
        
        # Check each column
        if not won:
            for i in range(self.boardSize):
                won = True
                for j in range(self.boardSize):
                    if self.marks[j][i]!=mark:
                        won=False
                        break
                if won:
                    break

        # Check first diagonal
        if not won:
            for i in range(self.boardSize):
                won = True
                if self.marks[i][i]!=mark:
                    won=False
                    break
                
        # Check second diagonal
        if not won:
            for i in range(self.boardSize):
                won = True
                if self.marks[self.boardSize-1-i][i]!=mark:
                    won=False
                    break

        return won
    
    # Determines whether the board is full
    # If full, returns True, and False otherwise
    def noMoreMoves(self):  # may need to be modified or overriden by min max
        return (self.marks!=' ').all()

    # This function
    def alphaBetaSearch(self):
        #v ←MAX-VALUE(state,−∞,+∞)
        #return the action in ACTIONS(state) with value v

        (value, row, col) = self.maxValue(-2, 2)

        return (row, col)

    def maxValue(self, alpha, beta):
        # initialize values
        maxValue = -2 
        row = None
        col = None
        utility = 2

        # checkWin to get the current utility and determine if the game is over
        playerWin = self.checkWin('X')
        computerWin = self.checkWin('O')

        if(playerWin == False) and (computerWin == False):
            utility = 0
        elif playerWin == True:
            utility = -1
        elif computerWin == True:
            utility = 1

        for i in range(0,3):
            for j in range(0,3):
                if self.marks[i][j] == ' ':
                    self.marks[i][j] = 'O'
                    (move, min_i, min_j) = self.minValue(alpha, beta)
                    if move > maxValue:
                        maxValue = move
                        row = i
                        col = j
                    self.marks[i][j] = ' '

                    if maxValue >= beta:
                        return (maxValue, row, col)

                    if maxValue > alpha:
                        alpha = maxValue

        return (maxValue, row, col)

    def minValue(self,alpha, beta):
        # initialize values
        minValue = 2 
        row = None
        col = None
        utility = 2

        # checkWin to get the current utility and determine if the game is over
        playerWin = self.checkWin('X')
        computerWin = self.checkWin('O')

        if(playerWin == False) and (computerWin == False):
            utility = 0
        elif playerWin == True:
            utility = -1
        elif computerWin == True:
            utility = 1

        for i in range(0,3):
            for j in range(0,3):
                if self.marks[i][j] == ' ':
                    self.marks[i][j] = 'X'
                    (move, max_i, max_j) = self.maxValue(alpha, beta)
                    if move < minValue:
                        minValue = move
                        row = i
                        col = j
                    self.marks[i][j] = ' '

                    if minValue <= alpha:
                        return (minValue, row, col)

                    if minValue < beta:
                        beta = minValue

        return (minValue, row, col)


    # Then make best move for the computer by placing the mark in the best spot
    def makeCompMove(self):

        (row, col) = self.alphaBetaSearch()

        self.makeMove(row, col, 'O')
        print("Computer chose: "+str(row)+","+str(col))
        

# Print out the header info
print("CLASS: Artificial Intelligence, Lewis University")
print("NAME: Christian Nelson")

LOST = 0
WON = 1
DRAW = 2
wrongInput = False
boardSize = int(input("Please enter the size of the board n (e.g. n=3,4,5,...): "))
        
# Create the game board of the given size
board = GenGameBoard(boardSize)
        
board.printBoard()  # Print the board before starting the game loop
        
# Game loop
while True:
    # *** Player's move ***        
    
    # Try to make the move and check if it was possible
    # If not possible get col,row inputs from player    
    row, col = -1, -1
    while not board.makeMove(row, col, 'X'):
        print("Player's Move")
        row, col = input("Choose your move (row, column): ").split(',')
        row = int(row)
        col = int(col)

    # Display the board again
    board.printBoard()
            
    # Check for ending condition
    # If game is over, check if player won and end the game
    if board.checkWin('X'):
        # Player won
        result = WON
        break
    elif board.noMoreMoves():
        # No moves left -> draw
        result = DRAW
        break
            
    # *** Computer's move ***
    board.makeCompMove()
    
    # Print out the board again
    board.printBoard()    
    
    # Check for ending condition
    # If game is over, check if computer won and end the game
    if board.checkWin('O'):
        # Computer won
        result = LOST
        break
    elif board.noMoreMoves():
        # No moves left -> draw
        result = DRAW
        break
        
# Check the game result and print out the appropriate message
print("GAME OVER")
if result==WON:
    print("You Won!")            
elif result==LOST:
    print("You Lost!")
else: 
    print("It was a draw!")

