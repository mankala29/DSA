#The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)
#P   A   H   N
#A P L S I I G
#Y   I   R
#And then read line by line: "PAHNAPLSIIGYIR"   
#Write the code that will take a string and make this conversion given a number of rows:
#string s = "PAYPALISHIRING", numRows = 3
#Output: "PAHNAPLSIIGYIR"   

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        rows = [""] * numRows
        current_row = 0
        direction = 0

        #if only one character in the string
        if numRows == 1:
            return s
        #use direction as a variable to move down +1 and up -1
        for i in s:
            rows[current_row] += i
            if current_row == 0:
                direction = +1
            elif current_row == numRows-1:
                direction = -1
            current_row += direction
        
        return "".join(rows)