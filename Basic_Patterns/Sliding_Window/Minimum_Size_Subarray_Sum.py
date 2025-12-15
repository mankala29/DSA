# Given an array of positive integers nums and a positive integer target, return the minimal length of a subarray whose sum is greater than or equal to target. 
# If there is no such subarray, return 0 instead.
# Example 1:
# Input: target = 7, nums = [2,3,1,2,4,3]
# Output: 2
# Explanation: The subarray [4,3] has the minimal length under the problem constraints.

class Solution(object):
    def minSubArray(self, nums, target):
        left = right = 0
        current_total = 0
        min_length = float('inf')
        while right < len(nums):
            current_total += nums[right]
            right += 1
            while current_total >= target:
                min_length = min(min_length, right - left)
                current_total -= nums[left]
                left += 1
        if min_length == float('inf'):
            return 0
        return min_length