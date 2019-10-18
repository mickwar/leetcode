# https://leetcode.com/problems/minimum-path-sum/


# This is an incorrect solution
class Solution:
    def minPathSum(self, grid):
        # Greedy search (always choose the lowest value)
        n = len(grid)       # rows
        m = len(grid[0])    # columns
        x = 0               # position in path
        y = 0               # position in path
        out = 0
        
        while x < n - 1 or y < m - 1:
            if x == n - 1:
                out += grid[x][y+1]
                y += 1
            elif y == m - 1:
                out += grid[x+1][y]
                x += 1
            else:
                if grid[x][y+1] > grid[x+1][y]:
                    out += grid[x+1][y]
                    x += 1
                else:
                    out += grid[x][y+1]
                    y += 1
                    
        # Add the last cell
        out += grid[x][y]
                    
        return out
    
