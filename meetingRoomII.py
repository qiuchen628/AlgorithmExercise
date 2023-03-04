class Solution:
    def minMeetingRooms(self, interval):
        end, rooms = 0, 0
        starts = sorted(i[0] for i in interval)
        ends = sorted(i[1] for i in interval)

        for i in range(len(starts)):
            if starts[i] < ends[end]:
                rooms += 1
            else:
                end += 1

        return rooms

intervals_example = [[1, 10], [11, 15], [3, 6],[22, 35], [31, 34], [33, 35]]

test_case = Solution()
res = test_case.minMeetingRooms(intervals_example)
print('number of meeting room is: ', res)

