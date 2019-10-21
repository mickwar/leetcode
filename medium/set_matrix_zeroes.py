# https://leetcode.com/problems/set-matrix-zeroes/zeroes
# At time of submission
#   performed 9% faster
#   used less than 5% memory
# than other solutions

class Solution:
    def setZeroes(self, matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        pos = []
        # Find coordinates for all zeros
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    pos.append([i, j])

        # Modify rows and columns of zeros found
        for p in pos:
            for i in range(m):
                matrix[i][p[1]] = 0
            for j in range(n):
                matrix[p[0]][j] = 0
