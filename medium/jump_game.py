# https://leetcode.com/problems/jump-game/
# At time of submission
#   performed 95% faster
#   used less than 7% memory
# than other solutions

class Solution:
    def canJump(self, nums):

        # Work backwords, always determining where a successful
        # jump may have originated
        index = len(nums) - 1
        for i in range(index, -1, -1):
            index = i if i + nums[i] >= index else index

        # Sequence of jumps can be made if index arrives at 0
        return True if index == 0 else False
