# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.
# Example 1:

# Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].

class Solution(object):
    def mergeIntervals(self, intervals):
        intervals.sort(key=lambda x:x[0])
        merged = [intervals[0]]

        for start, end in intervals[1:]:
            last_end = merged[-1][-1]

            if end < last_end:
                merged[-1][-1] = max(last_end, end)
            else:
                merged.append(start, end)
        return merged