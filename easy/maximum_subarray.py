# https://leetcode.com/problems/maximum-subarray/submissions/
# At time of submission
#   performed 78% faster
#   used less than 5% memory
# than other solutions

class Solution:
    def maxSubArray(self, nums):
        # Empty list, return 0
        if len(nums) == 0:
            return 0
        
        # All non-negative, return sum of the list
        if min(nums) >= 0:
            return sum(nums)
        
        # All non-positive, return largest value
        if max(nums) <= 0:
            return max(nums)
        
        current_sum = nums[0]
        best_sum = nums[0]
        for i in range(1, len(nums)):
            # Increase the current sum or reset it to current number.
            # When a reset occurs, the previous contiguous subarray has reached
            # its largest value, and we might need to check another subarray.
            current_sum = max(current_sum + nums[i], nums[i])
            best_sum = max(best_sum, current_sum)
            
        return best_sum


# Example
obj = Solution()
print(obj.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
print(obj.maxSubArray([-2,1,-3,4,-1,2,1,-5,4,-15,10]))
