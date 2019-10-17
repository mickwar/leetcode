# https://leetcode.com/problems/climbing-stairs/
# At time of submission
#   performed 89% faster
#   used less than 5% memory
# than other solutions

# Climb stairs that are n steps high. On each step, you can go either 1 or 2
# steps. How many distinct ways can you climb to the stop?

# The trick was just recognizing that the number of distinct ways was just
# the Fibonacci sequence.

# This can be improved using the Fibonacci formula to calculate the nth number
# directly by using the sequence's relationship with the golden ratio, or using
# Binet's method.

class Solution:
    def climbStairs(self, n):
        y, x = 1, 0
        for i in range(n):
            y, x = x + y, y
        return y
        

### List of distinct ways to climb
# 0 = 1 (?)
# 1 = 1
#   1
# 2 = 2
#   1 + 1
#   2
# 3 = 3
#   1 + 1 + 1
#   1 + 2
#   2 + 1
# 4 = 5
#   1 + 1 + 1 + 1
#   1 + 1 + 2
#   1 + 2 + 1
#   2 + 1 + 1
#   2 + 2
# 5 = 8
#   1 + 1 + 1 + 1 + 1
#   1 + 1 + 1 + 2
#   1 + 1 + 2 + 1
#   1 + 2 + 1 + 1
#   2 + 1 + 1 + 1
#   1 + 2 + 2
#   2 + 1 + 2
#   2 + 2 + 1
# 6 = 13
#   1 + 1 + 1 + 1 + 1 + 1
#   1 + 1 + 1 + 1 + 2
#   1 + 1 + 1 + 2 + 1
#   1 + 1 + 2 + 1 + 1
#   1 + 2 + 1 + 1 + 1
#   2 + 1 + 1 + 1 + 1
#   1 + 1 + 2 + 2
#   1 + 2 + 1 + 2
#   2 + 1 + 1 + 2
#   1 + 2 + 2 + 1
#   2 + 1 + 2 + 1
#   2 + 2 + 1 + 1
#   2 + 2 + 2
# 7 = 21
#   1 + 1 + 1 + 1 + 1 + 1 + 1
#   1 + 1 + 1 + 1 + 1 + 2
#   1 + 1 + 1 + 1 + 2 + 1
#   1 + 1 + 1 + 2 + 1 + 1
#   1 + 1 + 2 + 1 + 1 + 1
#   1 + 2 + 1 + 1 + 1 + 1
#   2 + 1 + 1 + 1 + 1 + 1
#   1 + 1 + 1 + 2 + 2
#   1 + 1 + 2 + 1 + 2
#   1 + 2 + 1 + 1 + 2
#   2 + 1 + 1 + 1 + 2
#   1 + 1 + 2 + 2 + 1
#   1 + 2 + 1 + 2 + 1
#   2 + 1 + 1 + 2 + 1
#   1 + 2 + 2 + 1 + 1
#   2 + 1 + 2 + 1 + 1
#   2 + 2 + 1 + 1 + 1
#   1 + 2 + 2 + 2
#   2 + 1 + 2 + 2
#   2 + 2 + 1 + 2
#   2 + 2 + 2 + 1
