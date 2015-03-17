# -*- coding: utf8 -*-
'''
__author__ = 'dabay.wang@gmail.com'

149: Max Points on a Line
https://leetcode.com/problems/max-points-on-a-line/

Given n points on a 2D plane, find the maximum number of points that lie on the same straight line.

=== Comments by Dabay===
http://www.cnblogs.com/zuoyuan/p/3760628.html
'''

# Definition for a point
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

class Solution:
    # @param points, a list of Points
    # @return an integer
    def maxPoints(self, points):
        if len(points) <= 2:
            return len(points)

        res = 2
        for i in xrange(len(points)):
            slope = {'inf': 0}
            same_point_count = 0
            for j in xrange(len(points)):
                if j == i:
                    continue
                if points[i].x == points[j].x and points[i].y != points[j].y:
                    slope['inf'] += 1
                elif points[i].x != points[j].x:
                    k = 1.0 * (points[j].y - points[i].y) / (points[j].x - points[i].x)
                    if k not in slope:
                        slope[k] = 1
                    else:
                        slope[k] += 1
                else:
                    same_point_count += 1
            res = max(res, max(slope.values()) + 1 + same_point_count)
        return res


def main():
    sol = Solution()
    points = [Point(0,0), Point(-1,-1), Point(2,2)]
    print sol.maxPoints(points)


if __name__ == "__main__":
    import time
    start = time.clock()
    main()
    print "%s sec" % (time.clock() - start)