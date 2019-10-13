# https://leetcode.com/problems/valid-sudoku/
# At time of submission
#   performed 11% faster
#   used less than 5% memory
# than other solutions

# A "valid" sudoku puzzle is not necessarily solveable, there just
# aren't any repititions in rows, columns, or the 3x3 subgrids

class Solution:
    def isValidSudoku(self, board):
        self.board = board
        return self.rowChecks() and self.colChecks() and self.subGridChecks()
    
    def rowChecks(self):
        for i in range(9):
            for j in range(9):
                if self.board[i].count(str(j+1)) > 1:
                    return False
        return True
    
    def colChecks(self):
        for i in range(9):
            tmp = list(map(lambda x: x[i], self.board))
            for j in range(9):
                if tmp.count(str(j+1)) > 1:
                    return False
        return True
    
    def subGridChecks(self):
        for i in range(9):
            p, q = (i % 3) * 3, (i // 3) * 3
            subgrid = [item for l in  map(lambda x: x[p:(p+3)], self.board[q:(q+3)]) for item in l]
            for j in range(9):
                if subgrid.count(str(j+1)) > 1:
                    return False
        return True



### Example
board1 = [
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]

board2 = [
  ["8","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]

obj = Solution()
obj.isValidSudoku(board1)
obj.isValidSudoku(board2)

