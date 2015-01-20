# -*- coding: utf8 -*-
'''
__author__ = 'dabay.wang@gmail.com'

47: Permutations II
https://oj.leetcode.com/problems/permutations-ii/

Given a collection of numbers that might contain duplicates, return all possible unique permutations.

For example,
[1,1,2] have the following unique permutations:
[1,1,2], [1,2,1], and [2,1,1].

===Comments by Dabay===
生成排列。
既然有重复的，就维护一个hash来记录那些已经处理过的情况。没想到就过了OJ。但是用时比较多
应该有精妙的解法，等下次google一下。
'''

class Solution:
    # @param num, a list of integer
    # @return a list of lists of integers
    def permuteUnique(self, num):
        def permutation2(result, checked, per, rest):
            if len(rest) == 0:
                result.append(list(per))
                return
            for i in xrange(len(rest)):
                per.append(rest[i])
                r = rest[:i] + rest[i+1:]
                if str(per) not in checked:
                    checked[str(per)] = True
                    permutation2(result, checked, per, r)
                per.pop(-1)

        result = []
        checked = {}
        permutation2(result, checked, [], num)
        return result


def main():
    sol = Solution()
    nums = [1,1,1,1,2,3]
    print len(sol.permuteUnique(nums))


if __name__ == "__main__":
    import time
    start = time.clock()
    main()
    print "%s sec" % (time.clock() - start)