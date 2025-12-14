#Given two strings s and t, return true if t is an anagram of s, and false otherwise.
# Example 1:
# Input: s = "anagram", t = "nagaram"
# Output: true

class Solution(object):
    def validAnagram(self, s, t):
        sort_s = sorted(s)
        sort_t = sorted(t)

        if sort_s == sort_t:
            return True
        return False