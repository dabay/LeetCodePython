# -*- coding: utf8 -*-
'''
__author__ = 'dabay.wang@gmail.com'

56: Merge Intervals
https://oj.leetcode.com/problems/merge-intervals/

Given a collection of intervals, merge all overlapping intervals.

For example,
Given [1,3],[2,6],[8,10],[15,18],
return [1,6],[8,10],[15,18].

===Comments by Dabay===
这道题想起来比较简单，实现的时候恼火。
技巧在与，不是一个个地插入到已有的序列，而是把已有的序列插入到一个标杆Interval前面、交叉、后面。

对于每一个序列中的Interval，
    - 如果它的end比标杆的start小，插入到前面
    - 如果它的start比标杆的end大，插入到后面
    - 如果它和标杆有交集，更新标杆的start和end
'''
# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    # @param intervals, a list of Interval
    # @return a list of Interval
    def merge(self, intervals):
        def insert(interval, merged):
            new_merged = []
            i = 0
            s = interval.start
            e = interval.end
            while i < len(merged):
                if merged[i].end < s:
                    new_merged.append(merged[i])
                    i = i + 1
                    continue
                if e < merged[i].start:
                    new_merged = new_merged + [Interval(s, e)] + merged[i:]
                    break
                s = min(s, merged[i].start)
                e = max(e, merged[i].end)
                i = i + 1
            else:
                new_merged.append(Interval(s, e))
            return new_merged


        if len(intervals) <= 1:
            return intervals

        merged = [intervals[0]]
        i = 1
        while i < len(intervals):
            merged = insert(intervals[i], merged)
            i = i + 1

        return merged


def main():
    sol = Solution()
    i1 = Interval(2,3)
    i2 = Interval(4,5)
    i3 = Interval(2,2)
    i4 = Interval(15,18)
    intervals = [i1,i2,i3,i4]
    intervals = sol.merge(intervals)
    for interval in intervals:
        print "[%s, %s] " % (interval.start, interval.end),
    print


if __name__ == "__main__":
    import time
    start = time.clock()
    main()
    print "%s sec" % (time.clock() - start)


