# https://leetcode.com/problems/triangle/
# At time of submission
#   performed 95% faster
#   used less than 6% memory
# than other solutions

# Very comparable to the minimum sum paths problem

class Solution:
    def minimumTotal(self, triangle):
        n = len(triangle)

        totalCost = [[0 for i in range(j+1)] for j in range(n)]

        totalCost[0] = triangle[0]
        for i in range(1, n): 
            totalCost[i][0] = totalCost[i-1][0] + triangle[i][0]
            totalCost[i][-1] = totalCost[i-1][-1] + triangle[i][-1]

        for i in range(2, n): 
            for j in range(1, i): 
                totalCost[i][j] = triangle[i][j] + min(totalCost[i-1][j-1],
                                                       totalCost[i-1][j])

        return min(totalCost[-1])


### Example
triangle = [
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3],
 [3,6,2,3,0]
]

obj = Solution()
print(obj.minimumTotal(triangle))
