# -*- coding:utf-8 -*-

class Solution(object):

    class Interval:
        def __init__(self, s=0, e=0):
            self.start = s
            self.end = e
        def printInterval(self):
            print([self.start, self.end])

    def merge(self, intervals):
        '''
        LeetCode 56 Merge Intervals
        input:[[1,3],[2,6],[8,10],[15,18]]
        output:[[1,6], [8,10], [15,18]]
        :param intervals:
        :return:
        '''
        merged = []
        intervals.sort(key=lambda x:x.start)
        for interval in intervals:
            if not merged or merged[-1].end < interval.start:
                merged.append(interval)
            else:
                merged[-1].end = max(merged[-1].end, interval.end)
        return merged

    def insert(self, intervals, newInterval):
        '''
        LeetCode 57 Insert Interval
        input:[[1,3],[6,9]] newInterval=[2,5]
        output:[[1,5], [6,9]]
        :param intervals:
        :param nreInterval:
        :return:
        '''
        left, right = 0, len(intervals)-1

        # 找到不影响插入效果的前面的interval
        while left<len(intervals) and intervals[left].end < newInterval.start:
            left += 1

        # 找到不影响插入效果的后面的interval
        while right>=0 and intervals[right].start > newInterval.end:
            right -= 1

        if left<=right:
            newInterval.start = min(newInterval.start, intervals[left].start)
            newInterval.end = max(newInterval.end, intervals[right].end)

        return intervals[:left] + [newInterval] + intervals[right+1:]

if __name__ == "__main__":
    s = Solution()

    i1 = s.Interval(1,3)
    i2 = s.Interval(2,5)
    i3 = s.Interval(8,10)
    i4 = s.Interval(9,18)

    newInterval = s.Interval(5,7)
    # test merge intervals
    intervals =[i1, i2, i3, i4]
    merged = s.merge(intervals)
    for item in merged:
        s.Interval.printInterval(item)

    # test insert interval
    insertIntervals = s.insert(intervals, newInterval)
    for item in insertIntervals:
        s.Interval.printInterval(item)
