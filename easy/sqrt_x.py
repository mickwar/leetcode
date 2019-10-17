# https://leetcode.com/problems/sqrtx/
# At time of submission
#   performed 81% faster
#   used less than 6% memory
# than other solutions

class Solution:
    # This is based the Newton method for computing square roots
    # (Also called the Babylonian method or Heron's method)
    def mySqrt(self, x):

        if x == 0:
            return 0
        
        # Starting at y = x means our sequence of numbers will be decreasing
        y = x

        # We only want the integer part, so we terminate the sequence when a
        # difference greater than -1 is observed (Why? Not really sure, but
        # it works. My goal is to stop the sequence when the reduction no longer
        # affects the integer part. I initially tried < -0.1, but <= -1 worked,
        # too.)
        change = -1
        while change <= -1:
            newy = 0.5*(y + x/y)
            change = newy - y
            y = newy
            
        return int(y)

    # Easy solution from built-in functions
    #def mySqrt(self, x):
    #    return int(x ** 0.5)


# Example
obj = Solution()
obj.mySqrt(1000)
1000 ** 0.5
