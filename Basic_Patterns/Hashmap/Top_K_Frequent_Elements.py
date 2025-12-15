#Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
#Example 1:
#Input: nums = [1,1,1,2,2,3], k = 2
#Output: [1,2]

class Solution(object):
    def topK(self, nums,k):
        dictionary = {}
        result = []

        for s in nums:
            if s not in dictionary:
                dictionary[s] = 1
            else:
                dictionary[s] += 1

        sorted_pairs = sorted(dictionary.items(), key=lambda x:x[1], reverse=True)

        for i in range(k):
            result.append(sorted_pairs[i][0])
        return result