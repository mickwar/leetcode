# https://leetcode.com/problems/jump-game/
#
# This solution works, but takes too long

class Solution:
    def canJump(self, nums):
        
        if len(nums) == 1:
            return True
        
        index = 0
        jump_path = [0]
        while nums[0] > 0:
            # Check if cleared
            if index + nums[index] >= len(nums) - 1:
                return True
            
            # Do another jump (if possible)
            if nums[index] > 0:
                index = index + nums[index]
                jump_path.append(index)
            else:
                # Otherwise, go back a step in jump_path
                # And decrement the value in nums
                # (This ensures we look at the largest jump posssible and
                # work our way down until no more jumps)
                jump_path.pop()
                index = jump_path[-1]
                nums[index] -= 1
                
        return False
