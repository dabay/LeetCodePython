# -*- coding: utf8 -*-
'''
Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

For example,
If n = 4 and k = 2, a solution is:

[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
'''

class Solution:
    # @return a list of lists of integers
    def combine(self, n, k):
        def add_tails(result, temp_list, num_list, index, num_count):
            if num_count == 0:
                result.append(list(temp_list))
                return
            for i in xrange(index, len(num_list)+1-num_count):
                temp_list.append(num_list[i])
                add_tails(result, temp_list, num_list, i+1, num_count-1)
                temp_list.pop(-1)


        result = []
        num_list = [i for i in xrange(1, n+1)]
        add_tails(result, [], num_list, 0, k)
        return result


if __name__ == "__main__":
    s = Solution()
    print s.combine(4, 2)
