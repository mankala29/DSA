# Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same.
# Consider the number of unique elements in nums to be k​​​​​​​​​​​​​​. After removing duplicates, return the number of unique elements k.
# The first k elements of nums should contain the unique numbers in sorted order. The remaining elements beyond index k - 1 can be ignored.
# Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.
# Example 1:
# Input: nums = [1,1,2]
# Output: 2, nums = [1,2,_] 

class Solution(object):
    def removeDuplicates(self, nums):
        left = right = 1
        while right < len(nums):
            if nums[right] != nums[right-1]:
                nums[left] = nums[right]
                left += 1
            right += 1
        return left