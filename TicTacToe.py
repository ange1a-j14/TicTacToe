class Board:
   def __init__(self):
      self.board = [ ["_", "_", "_"],
                     ["_", "_", "_"],
                     ["_", "_", "_"]
                  ]  
   
   def display(self):
      print("_____________", end='') #9 underscores
      for row in self.board:
         print("\n|", end='')
         for el in row:
            print("_" + el + "_|", end='')
   
   def updateBoard(self, move, row, col):
      self.board[row][col] = move

class GameControl:
   def __init__(self, board, player1Name="Player 1", player2Name = "Player 2"):
      self.board = board
      self.currPlayer = player1Name
      self.nextPlayer = player2Name
   
   def updateCurrPlayer(self):
      currPlayer = player2Name if currPlayer == player1Name else player1Name
      nextPlayer = player2Name if nextPlayer == player1Name else player2Name

   def makeMove(self):
      #get user input and update board
      self.board.display()
      self.updateCurrPlayer()

   #def gameOver(self):
      

   #def newGame(self):
   #   while not(gameOver):

board = Board()
board.updateBoard("x", 0, 0)
board.display()