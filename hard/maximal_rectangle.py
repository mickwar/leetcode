# https://leetcode.com/problems/maximal-rectangle/
#
# This solution works (I believe), but is inefficient and times out
# when judging on leetcode.
#
# Need to look into dynamic programming and stacks

class Solution:
    def maximalRectangle(self, matrix):
        """
            The general algorithm used here:
                1. Calculate the cumulative row sums for the given matrix,
                   where the sum resets when a "0" is encountered.
                2. For each row in the matrix, do the following:
                    a. Set diff = 0.
                    b. Find all sublists of consecutive, non-zeros entries
                       having a range (max - min) no greater than diff.
                    c. The "area" for each sublist is computed as
                       area = length(list) * min(list).
                    d. Repeat steps a - c until diff equals the row number.
                3. Return the largest computed area.

            The trick in part b is to recognize that min(list) is the height
            of the rectangle. For example, a sublist like [1, 2, 1] means that
            the original matrix looked something like [[0, 1, 0], [1, 1, 1]].
        """
        if len(matrix) == 0:
            return 0
        
        self.rowSum(matrix)
        if sum([sum(l) for l in self.rowsums]) == 0:
            return 0
        
        maxArea = 0
        
        for ii in range(self.n):
            ll = self.rowsums[ii]
            tmp1 = []   # List of all sublists
            tmp2 = []   # Where each sublist is built individually
            for diff in range(ii + 1):
                for i in range(self.k):
                    if ll[i] == 0:
                        continue
                    if len(tmp2) == 0:
                        tmp2 = [ll[i]]
                    for j in range(i+1, self.k):
                        if ll[j] == 0:
                            if tmp2 not in tmp1:
                                tmp1.append(tmp2)
                            tmp2 = []
                            break
                        # Only add the candidate value if within the appropriate range
                        # Otherwise, the sublist is ended
                        if max(abs(max(tmp2) - ll[j]), abs(min(tmp2) - ll[j])) <= diff:
                            tmp2.append(ll[j])
                        else:
                            if tmp2 not in tmp1:
                                tmp1.append(tmp2)
                            tmp2 = []
                            break
                    if len(tmp2) != 0:
                        if tmp2 not in tmp1:
                            tmp1.append(tmp2)
                        tmp2 = []

            areas = [len(l) * min(l) for l in tmp1]
            if len(areas) > 0:
                maxArea = max(maxArea, max(areas))
            
        return maxArea

    # Calculate cumulative row sums, with resets at 0
    # So
    #   [[1, 0, 1, 1],
    #    [1, 1, 0, 1],
    #    [1, 1, 1, 0]]
    # becomes
    #   [[1, 0, 1, 1],
    #    [2, 1, 0, 2],
    #    [3, 2, 1, 0]]
    def rowSum(self, matrix):
        self.n, self.k = len(matrix), len(matrix[0])
        self.rowsums = [[0] * self.k for _ in range(self.n)]
        self.rowsums[0] = [1 if m == '1' else 0 for m in matrix[0]]
        for i in range(1, self.n):
            for j in range(self.k):
                self.rowsums[i][j] = (1 if matrix[i][j] == '1' else 0) * (self.rowsums[i-1][j] + 1)


### Example
matrix = [
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
]

obj = Solution()
print(obj.maximalRectangle(matrix))
