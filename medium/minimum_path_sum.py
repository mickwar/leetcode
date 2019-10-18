# https://leetcode.com/problems/minimum-path-sum/

# Thanks to this article for help: https://www.geeksforgeeks.org/min-cost-path-dp-6/
# Naive recursion, works but takes too long
import sys
class Solution:
    def minPathSum(self, grid):
        n = len(grid)       # rows
        m = len(grid[0])    # columns
        # Working our way backward, from the end to the start
        return self.minCostToXY(grid, n - 1, m - 1)
        
    def minCostToXY(self, grid, x, y):
        # Return very large value if out of bounds
        if x < 0 or y < 0:
            return sys.maxsize
        elif x == 0 and y == 0:
            return grid[x][y]
        else:
            # We can only go down and right, hence the two branches.
            # This is where the recursion goes down. It needs to follow each
            # path until it can come back up and compute the minimums.
            return grid[x][y] + min(self.minCostToXY(grid, x, y-1),
                                    self.minCostToXY(grid, x-1, y))



obj = Solution()

grid = [
  [1,3,1,0],
  [1,5,1,0],
  [4,2,1,1]
]
print(obj.minPathSum(grid))


grid = [
  [1,3,1,0],
  [1,5,1,0],
  [0,0,1,1]
]
print(obj.minPathSum(grid))
