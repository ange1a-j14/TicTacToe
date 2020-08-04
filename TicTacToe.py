import random

class Board:
   #create either 3x3 empty board or 3x3 example board with position numbers
   def __init__(self, board="empty"):
      self.board = [["_", "_", "_"],["_", "_", "_"],["_", "_", "_"]] if board=="empty" else [["0", "1", "2"], ["3", "4", "5"], ["6", "7", "8"]]
      self.booleanboard = [[False, False, False],[False, False, False],[False, False, False]]
   
   def display(self):
      print("\n_____________", end='') #9 underscores
      for row in self.board:
         print("\n|", end='')
         for el in row:
            print("_" + el + "_|", end='')
   
   def updateBoard(self, move, row, col):
      self.board[row][col] = move
      self.booleanboard[row][col] = True

   def checkRows(self):
      for row in range(3):
         if self.board[row][0] != "_" and self.board[row][0] == self.board[row][1] and self.board[row][0] == self.board[row][2]:
            return True
      return False

   def checkCols(self):
      for col in range(3):
         if self.board[0][col] != "_" and self.board[0][col] == self.board[1][col] and self.board[0][col] == self.board[2][col]:
            return True
      return False

   def checkDiags(self):
      return (self.board[0][0] != "_" and self.board[0][0] == self.board[1][1] and self.board[0][0] == self.board[2][2]) or (self.board[0][2] != "_" and self.board[0][2] == self.board[1][1] and self.board[0][2] == self.board[2][0])

   def isFilled(self):
      for row in range(3):
         for col in range(3):
            if self.board[row][col] == "_": return False
      return True

   def clearBoard(self):
      for row in range(3):
         for col in range(3):
            self.board[row][col] = "_"
            self.booleanboard[row][col] = False

class GameControl:
   def __init__(self, board, player1Name="Player 1", player2Name = "Player 2", autoOpponent = False):
      self.board = board
      self.player1Name = player1Name
      self.player2Name = player2Name
      self.currPlayer = player1Name
      self.nextPlayer = player2Name
      self.autoOpponent = autoOpponent
   
   def updateCurrPlayer(self):
      temp = self.currPlayer
      self.currPlayer = self.nextPlayer
      self.nextPlayer = temp

   def makeMove(self):
      if(self.autoOpponent and self.currPlayer == self.player2Name):
         self.makeMoveAuto()
         return
      example = Board("number")
      example.display()
      position = int(input("\n" + self.currPlayer + ", please select a number corresponding to a position on the board.\n"))
      while (position < 0 or position > 8) or self.isTaken(position):
         example.display()
         print("\nThat was not a valid position.")
         try:
            position = int(input("\n" + self.currPlayer + ", please select a valid position.\n"))
         except:
            position = -1
      rowCol = self.findPosition(position)
      self.board.updateBoard("x" if self.currPlayer == self.player1Name else "o", rowCol[0], rowCol[1])
      self.board.display()

   def makeMoveAuto(self):
      position = random.randint(0, 8)
      while (self.isTaken(position)):
         position = random.randint(0, 8)
      rowCol = self.findPosition(position)
      self.board.updateBoard("o", rowCol[0], rowCol[1])
      self.board.display()
   #precondition: position E [0, 8]
   def findPosition(self, position):
      if position < 3: return [0, position]
      elif position < 6: return [1, position - 3]
      else: return [2, position - 6]

   def isTaken(self, position):
      rowCol = self.findPosition(position)
      return self.board.booleanboard[rowCol[0]][rowCol[1]]

   def gameOver(self):
      if self.board.checkRows() or self.board.checkCols() or self.board.checkDiags():
         print("\n" + self.nextPlayer, "has won!")
         return True
      if self.board.isFilled():
         print("\n", self.player1Name, "and", self.player2Name, "have tied!")
         return True

   def newGame(self):
      while not(self.gameOver()):
         self.makeMove()
         self.updateCurrPlayer()
      playAgain = "a"
      while playAgain != "y" and playAgain != "n":
         playAgain = input("Would you like to play again? (y/n)\n")
      if playAgain == "y": 
         self.board.clearBoard()
         self.newGame()
      else: print("Thanks for playing!")

player1 = input("Who is player one?\n")
while auto != "y" and auto != "n":
         auto = input("Is there a player two? (y/n)\n")
if (not auto):
   player2 = input("Who is player two?\n")
game = GameControl(Board(), player1, player2 if not auto else "Computer", auto)
game.newGame()