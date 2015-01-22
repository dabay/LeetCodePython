# -*- coding: utf8 -*-
'''
__author__ = 'dabay.wang@gmail.com'

57: Insert Interval
https://oj.leetcode.com/problems/insert-interval/

Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).
You may assume that the intervals were initially sorted according to their start times.

Example 1:
Given intervals [1,3],[6,9], insert and merge [2,5] in as [1,5],[6,9].

Example 2:
Given [1,2],[3,5],[6,7],[8,10],[12,16], insert and merge [4,9] in as [1,2],[3,10],[12,16].

This is because the new interval [4,9] overlaps with [3,5],[6,7],[8,10].

===Comments by Dabay===
这道题应该在放在Merge Interval那道题之前才对。
关键是如何插入的问题：
    如果用需要插入的Interval去判断它与已有序列重叠的情况比较复杂。
    所以，就新建一个新的序列，把以后的序列一个个往里面放，放的时候判断它与需要插入的那个Interval之间的关系。
'''
# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    # @param intervals, a list of Intervals
    # @param newInterval, a Interval
    # @return a list of Interval
    def insert(self, intervals, newInterval):
        new_intervals = []
        i = 0
        s = newInterval.start
        e = newInterval.end
        while i < len(intervals):
            if intervals[i].end < s:
                new_intervals.append(intervals[i])
                i = i + 1
                continue
            if e < intervals[i].start:
                new_intervals = new_intervals + [Interval(s, e)] + intervals[i:]
                break
            s = min(intervals[i].start, s)
            e = max(intervals[i].end, e)
            i = i + 1
        else:
            new_intervals.append(Interval(s, e))
        return new_intervals


def main():
    sol = Solution()
    i1 = Interval(1,3)
    i2 = Interval(6,9)
    i3 = Interval(2,2)
    i4 = Interval(15,18)
    intervals = [i1,i2]
    intervals = sol.insert(intervals, Interval(2, 5))
    for interval in intervals:
        print "[%s, %s] " % (interval.start, interval.end),
    print


if __name__ == "__main__":
    import time
    start = time.clock()
    main()
    print "%s sec" % (time.clock() - start)


