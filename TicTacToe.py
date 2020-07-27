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

board = Board()
board.updateBoard("x", 0, 0)
board.display()