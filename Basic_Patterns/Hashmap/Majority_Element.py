#Given an array nums of size n, return the majority element.
#The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.
#Example 1:
#Input: nums = [3,2,3]
#Output: 3  

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dictionary = {}
        req_len = len(nums)/2

        for i in nums:
            if i not in dictionary:
                dictionary[i] = 1
            elif i in dictionary:
                dictionary[i] += 1
        
            if dictionary[i] > req_len:
                return i
        return -1