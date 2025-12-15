# Given an array of meeting time intervals where intervals[i] = [starti, endi], determine if a person could attend all meetings.
# Example 1:
# Input: intervals = [[0,30],[5,10],[15,20]]
# Output: false
# Example 2:
# Input: intervals = [[7,10],[2,4]]
# Output: true

class Solution(object):
    def meetRooms(self, intervals):
        sorted_intervals = sorted(intervals, key=lambda x: x[0])

        for i in range(1, len(sorted_intervals)):
            prev_start, prev_end = intervals[i-1]
            curr_start, curr_end = intervals[i]

            if curr_start < prev_end:
                return False
        return True