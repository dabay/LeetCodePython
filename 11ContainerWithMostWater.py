# -*- coding: utf8 -*-
'''
https://oj.leetcode.com/problems/container-with-most-water/

Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai).
n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0).
Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container.

===Comments by Dabay===
这道题很经典。
原理：固定一根长杆子X的时候，最远端的一个短杆子Y，此时是Y能围住的最大容积。所以Y的全部可能都考虑进去了。可以考虑第二远的杆子了。
也就是说，先选择两端的杆子，固定长的那一个（因为长的杆子可能与另外某根杆子围成更大的容积），移动短的那个（因为以短的杆子能围住的最大可能容积，
就是在移动之前，与长杆围成的）。

两个指针，一个方向从左到右，另一个方向从右到左。
计算最大容量，更新max_area。
然后移动，小数的指针（即：如果左指针的数比右指针的数小，左指针往右移动，进入下一次计算；反之，右指针往左移动，进入下一次计算）
当两个指针遇到的时候退出。

这里的代码不是优美的，完全是为了跑个OJ靠前的位置。这基本上是python最靠前的成绩了。109ms。
'''
class Solution:
    # @return an integer
    def maxArea(self, height):
        max_area = 0
        i, j = 0, len(height) - 1
        while i < j:
            if height[i] < height[j]:
                right_taller, short, short_index = True, height[i], i
            else:
                right_taller, short, short_index = False, height[j], j

            area = short * (j-i)
            if area > max_area:
                max_area = area

            if right_taller:
                i = i + 1
                while height[i] < short:
                    i = i + 1
            else:
                j = j - 1
                while height[j] < short:
                    j = j - 1
        return max_area


def main():
    s = Solution()
    print s.maxArea([1,2,5,1,4,1])


if __name__ == "__main__":
    import time
    start = time.clock()
    main()
    print "%s sec" % (time.clock() - start)