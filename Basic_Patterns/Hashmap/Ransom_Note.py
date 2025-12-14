#Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.
#Each letter in magazine can only be used once in ransomNote.
#Example 1:
#Input: ransomNote = "a", magazine = "b"
#Output: false

class Solution(object):
    def ransomNote(self, ransomeNote, magazine):

        dictionary = {}

        for s in magazine:
            if s not in dictionary:
                dictionary[s] = 1
            dictionary[s] += 1

        for s in ransomeNote:
            if s not in dictionary or dictionary[s] == 0:
                return False
            dictionary[s] -= 1
        return True