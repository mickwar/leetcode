# https://leetcode.com/problems/jump-game/
#
# This solution works, but takes too long

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
        current_index = next(ind for ind, val in enumerate(max_jump) if val >= last_index) 
        
        # Where the penultimate jump can be made
        previous_index = next(ind for ind, val in enumerate(max_jump) if val >= current_index) 
        
        while previous_index < current_index:
            current_index = previous_index
            previous_index = next(ind for ind, val in enumerate(max_jump) if val >= current_index) 
            
        if current_index == 0:
            return True
        else:
            return False
