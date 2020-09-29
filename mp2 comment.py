""" 
Christian Nelson
9/29/2020
CPSC-57100-002, Fall 2020
Machine Problem 2: Tic-Tac-Toe
"""


import numpy as np
import random
import math

class GenGameBoard: 
    def __init__(self, boardSize):
        self.boardSize = boardSize
        self.marks = np.empty((boardSize, boardSize),dtype='str')
        self.marks[:,:] = ' '

    def printBoard(self): 
        print(' ',end='')
        for j in range(self.boardSize):
            print(" "+str(j+1), end='')
        
        print("")
        for i in range(self.boardSize):
            print(" ",end='')
            for j in range(self.boardSize):
                print("--",end='')
            
            print("-")

            print(i+1,end='')
            
            for j in range(self.boardSize):
                print("|"+self.marks[i][j],end='')
            
            print("|")
                
        print(" ",end='')
        for j in range(self.boardSize):
            print("--",end='')
        
        print("-")
    
    def makeMove(self, row, col, mark):
        possible = False
        if row==-1 and col==-1:
            return False

        row = row - 1
        col = col - 1
        
        if row<0 or row>=self.boardSize or col<0 or col>=self.boardSize:
            print("Not a valid row or column!")
            return False

        if self.marks[row][col] == ' ':
            self.marks[row][col] = mark
            possible = True    

        if not possible and mark=='X':
            print("\nself position is already taken!")
        
        return possible
    
    def checkWin(self, mark):
        won = False 

        for i in range(self.boardSize):
            won = True
            for j in range(self.boardSize):
                if self.marks[i][j]!=mark:
                    won=False
                    break        
            if won:
                break
        
        if not won:
            for i in range(self.boardSize):
                won = True
                for j in range(self.boardSize):
                    if self.marks[j][i]!=mark:
                        won=False
                        break
                if won:
                    break

        if not won:
            for i in range(self.boardSize):
                won = True
                if self.marks[i][i]!=mark:
                    won=False
                    break
                
        if not won:
            for i in range(self.boardSize):
                won = True
                if self.marks[self.boardSize-1-i][i]!=mark:
                    won=False
                    break

        return won

    def noMoreMoves(self):
        return (self.marks!=' ').all()

    
    # TODO
    def makeCompMove(self):
        row, col = -1, -1
        while not self.makeMove(row, col, 'O'):
            col = random.randint(1,boardSize)
            row = random.randint(1,boardSize)
        print("Computer chose: "+str(row)+","+str(col))

print("CLASS: Artificial Intelligence, Lewis University")
print("NAME: Christian Nelson")

LOST = 0
WON = 1
DRAW = 2    
wrongInput = False
boardSize = int(input("Please enter the size of the board n (e.g. n=3,4,5,...): "))
        

board = GenGameBoard(boardSize)
        
board.printBoard() 
        

while True:     
    row, col = -1, -1
    while not board.makeMove(row, col, 'X'):
        print("Player's Move")
        row, col = input("Choose your move (row, column): ").split(',')
        row = int(row)
        col = int(col)

    board.printBoard()
            
    if board.checkWin('X'):
        result = WON
        break
    elif board.noMoreMoves():
        result = DRAW
        break
            
    board.makeCompMove()
    
    board.printBoard()    
    
    if board.checkWin('O'):
        result = LOST
        break
    elif board.noMoreMoves():
        result = DRAW
        break
        
print("GAME OVER")
if result==WON:
    print("You Won!")            
elif result==LOST:
    print("You Lost!")
else: 
    print("It was a draw!")

