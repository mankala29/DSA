# Given an array of intervals intervals where intervals[i] = [starti, endi], return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.
# Note that intervals which only touch at a point are non-overlapping. For example, [1, 2] and [2, 3] are non-overlapping.

# Example 1:

# Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
# Output: 1
# Explanation: [1,3] can be removed and the rest of the intervals are non-overlapping.

class Solution(object):
    def eraseIntervals(self, intervals):

        intervals.sort(key=lambda x:x[1])
        prev_end = intervals[0][1]
        counter = 0

        for start, end in intervals[1:]:
            if start < prev_end:
                counter += 1
            else:
                prev_end = end
        return counter