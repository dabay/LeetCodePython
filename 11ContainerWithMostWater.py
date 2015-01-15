# -*- coding: utf8 -*-
'''
https://oj.leetcode.com/problems/container-with-most-water/

Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai).
n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0).
Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container.

===Comments by Dabay===
这道题很经典，但是我还是不知道为什么可以。姑且就记住解法吧，茴香豆的写法也会一种。

两个指针，一个方向从左到右，另一个方向从右到左。
计算最大容量，更新max_area。
然后移动，小数的指针！！（即：如果左指针的数比右指针的数小，左指针往右移动，进入下一次计算；反之，右指针往左移动，进入下一次计算）
当遇到的时候退出。
'''
class Solution:
    # @return an integer
    def maxArea(self, height):
        max_area = 0
        i, j = 0, len(height) - 1
        while i < j:
            s = min(height[i], height[j]) * (j-i)
            max_area = max(s, max_area)
            if height[i] < height[j]:
                i = i + 1
            else:
                j = j - 1
        return max_area


def main():
    s = Solution()
    print s.maxArea([1,2,3,1,3,1])


if __name__ == "__main__":
    import time
    start = time.clock()
    main()
    print "%s sec" % (time.clock() - start)