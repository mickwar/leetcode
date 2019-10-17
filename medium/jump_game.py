# https://leetcode.com/problems/jump-game/
# At time of submission
#   performed 95% faster
#   used less than 7% memory
# than other solutions
# 


class Solution:
    def canJump(self, nums):
        
        if len(nums) == 1:
            return True
        
        # Get index for largest jump that can be made
        last_index = len(nums) - 1
        max_jump = [i + nums[i] for i in range(last_index)]
        
        if max(max_jump) < last_index:
            return False
        
        # Where the final jump can be made
        index = next(ind for ind, val in enumerate(max_jump) if val >= last_index) 
        
        # Now work backwards
        for i in range(index - 1, -1, -1):
            if max_jump[i] >= index:
                index = i
            
        if index == 0:
            return True
        else:
            return False
