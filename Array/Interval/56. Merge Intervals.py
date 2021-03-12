class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return intervals
        intervals.sort(key = lambda x:x[0])
        res = [intervals[0]]
        for i in range(1, len(intervals)):
            cur_start, cur_end = intervals[i]
            pre_end = res[-1][1]
            if pre_end >= cur_start:
                res[-1][1] = max(pre_end, cur_end)
            else:
                res.append([cur_start, cur_end])
        return res