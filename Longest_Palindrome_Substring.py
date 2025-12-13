#Given a string s, return the longest palindromic substring in s.

#Example 1:
#Input: s = "babad"
#Output: "bab"
#Explanation: "aba" is also a valid answer.

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        def expand(left, right):
            while left >= 0 and right < len(s):
                if s[left] != s[right]:
                    break
                left -= 1
                right += 1
            return left+1,right-1

        l1 = r1 = l2 = r2 = 0
        odd_length = even_length = 0
        best_left = best_right = best_length = 0

        for i in range(len(s)):
            l1, r1 = expand(i,i+1) #even
            l2, r2 = expand(i, i) #odd

            even_length = r1-l1+1
            odd_length = r2-l2+1

            if odd_length > best_length:
                best_left = l2
                best_right = r2
            if even_length > best_length:
                best_left = l1
                best_right = r1
            best_length = best_right-best_left+1
        return s[best_left:best_right+1]