#Given an array of string strs, group the anagrams together. You can return the answer in any order.
#An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
#Example 1:
#Input: strs = ["eat","tea","tan","ate","nat","bat"]
#Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs):

        dictionary = defaultdict(list)

        for word in strs:
            sorted_words = "".join(sorted(word))
            dictionary[sorted_words].append(word)
        return dictionary.values()