# https://leetcode.com/problems/minimum-path-sum/
# At time of submission
#   performed 78% faster
#   used less than 17% memory
# than other solutions

# Thanks to this article for help: https://www.geeksforgeeks.org/min-cost-path-dp-6/
# Using dynamic programming (DP), allocating memory so we don't do unnecessary
# computations. There is no recursion, we've optimized it out using DP.
class Solution:
    def minPathSum(self, grid):
        n = len(grid)       # rows
        m = len(grid[0])    # columns

        # We use a total cost array "tc" where tc[i][j] is the total (minimum)
        # cost to go from [0][0] up until [i][j]. Thus, the last element,
        # tc[n-1][m-1] is the minimum across all possible paths.

        ### Initialize total cost array
        # Initial space
        tc = [[0] * m for _ in range(n)]
        tc[0][0] = grid[0][0]

        # First column
        for i in range(1, n):
            tc[i][0] = tc[i-1][0] + grid[i][0]

        # First row
        for j in range(1, m):
            tc[0][j] = tc[0][j-1] + grid[0][j]

        # Fill in the remaining
        for i in range(1, n):
            for j in range(1, m):
                tc[i][j] = grid[i][j] + min(tc[i-1][j],
                                            tc[i][j-1])
        
        return tc[n-1][m-1]


### Examples
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
