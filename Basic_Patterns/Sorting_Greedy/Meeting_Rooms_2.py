# Given an array of meeting time intervals intervals where intervals[i] = [starti, endi], return the minimum number of conference rooms required.
# Example 1:
# Input: intervals = [[0,30],[5,10],[15,20]]
# Output: 2
# Example 2:
# Input: intervals = [[7,10],[2,4]]
# Output: 1

class Solution(object):
    def meetRooms2(self, intervals):
        start_times = sorted([x[0] for x in intervals])
        end_times = sorted([x[1] for x in intervals])

        i = j = 0
        max_rooms = rooms = 0

        while i < len(start_times):
            if start_times[i] < end_times[j]:
                rooms += 1
                i += 1
            else:
                rooms -= 1
                j += 1
            max_rooms = max(max_rooms, rooms)
        return max_rooms