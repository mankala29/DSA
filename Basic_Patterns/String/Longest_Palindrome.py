#Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.
#Letters are case sensitive, for example, "Aa" is not considered a palindrome.
#Example 1:
#Input: s = "abccccdd"
#Output: 7
#Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.

from collections import Counter
class Solution(object):
    def longestPalindrome(self, s):
        count = Counter(s)
        length = 0
        odd_found = False
        for i,c in count.items():
            if c%2 == 0:
                length += c
            else:
                length += c-1
                odd_found=True
        if odd_found:
            length += 1

        return length