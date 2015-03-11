# -*- coding: utf8 -*-
'''
__author__ = 'dabay.wang@gmail.com'

135: Candy
https://leetcode.com/problems/candy/

There are N children standing in a line. Each child is assigned a rating value.
You are giving candies to these children subjected to the following requirements:
    - Each child must have at least one candy.
    - Children with a higher rating get more candies than their neighbors.
What is the minimum candies you must give?

=== Comments by Dabay===
摘录自：http://blog.csdn.net/linhuanmars/article/details/21424783
这道题用到的思路和Trapping Rain Water是一样的，用动态规划。基本思路就是进行两次扫描，一次从左往右，一次从右往左。
第一次扫描的时候维护对于每一个小孩左边所需要最少的糖果数量，存入数组对应元素中，
第二次扫描的时候维护右边所需的最少糖果数，并且比较将左边和右边大的糖果数量存入结果数组对应元素中。
这样两遍扫描之后就可以得到每一个所需要的最最少糖果量，从而累加得出结果。
方法只需要两次扫描，所以时间复杂度是O(2*n)=O(n)。空间上需要一个长度为n的数组，复杂度是O(n)。
'''

class Solution:
    # @param ratings, a list of integer
    # @return an integer
    def candy(self, ratings):
        if len(ratings) == 0:
            return 0

        candy = [1 for _ in ratings]
        for i in xrange(1, len(ratings)):
            if ratings[i-1] < ratings[i]:
                candy[i] = candy[i-1] + 1

        count = candy[-1]
        for i in xrange(len(ratings)-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                candy[i] = max(candy[i+1] + 1, candy[i])
            count += candy[i]

        return count


def main():
    sol = Solution()
    rating = [2, 1]
    print sol.candy(rating)


if __name__ == "__main__":
    import time
    start = time.clock()
    main()
    print "%s sec" % (time.clock() - start)