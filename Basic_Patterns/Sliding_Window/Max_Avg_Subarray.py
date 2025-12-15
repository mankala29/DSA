# You are given an integer array nums consisting of n elements, and an integer k.
# Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.
# Example 1:
# Input: nums = [1,12,-5,-6,50,3], k = 4
# Output: 12.75000
# Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75

class Solution(object):
    def maxAvg(self, nums, k):

        left = 0
        right = k
        window_sum = sum(nums[:k])
        max_avg = window_sum/float(k)

        while right < len(nums):
            window_sum += nums[right]
            window_sum -= nums[left]
            right += 1
            left += 1

            max_avg = max(max_avg, window_sum/float(k))
        return max_avg