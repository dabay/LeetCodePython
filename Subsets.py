# -*- coding: utf8 -*-
'''
Given a set of distinct integers, S, return all possible subsets.

Note:
Elements in a subset must be in non-descending order.
The solution set must not contain duplicate subsets.
For example,
If S = [1,2,3], a solution is:

[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
'''
class Solution:
    # @param S, a list of integer
    # @return a list of lists of integer
    def subsets(self, S):
        def get_subsets(result, subset, i, index, new_list):
            if i == 0:
                result.append(list(subset))
                return
            for j in xrange(index, len(S)+1-i):
                subset.append(S[j])
                get_subsets(result, subset, i-1, j+1, new_list)
                subset.pop(-1)

        def process_list(S):
            # Sort
            list.sort(S)
            # Delete duplicated items
            index = 0
            for i in xrange(1, len(S)):
                if S[index] == S[i]:
                    continue
                index = index + 1
                (S[index], S[i]) = (S[i], S[index])
            return S[:index+1]

        result = [[]]
        if len(S) == 0:
            return  result
        new_list = process_list(S)
        for i in xrange(1, len(new_list)+1):
            get_subsets(result, [], i, 0, new_list)
        return result


if __name__ == "__main__":
    s = Solution()
    num_list = [4,1,0]
    print s.subsets(num_list)