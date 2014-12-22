# -*- coding: utf8 -*-
'''
Given a collection of integers that might contain duplicates, S, return all possible subsets.

Note:
Elements in a subset must be in non-descending order.
The solution set must not contain duplicate subsets.
For example,
If S = [1,2,2], a solution is:

[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]
实力差啊，只能用比较笨的办法。。。  修炼中~
'''

class Solution:
    # @param num, a list of integer
    # @return a list of lists of integer
    def subsetsWithDup(self, S):
        def dfs(result, S, index, l):
            if index == len(S)-1:
                l.append(S[index])
                result.append(list(l))
                l.pop(-1)
                result.append(list(l))
                return

            l.append(S[index])
            dfs(result, S, index+1, l)
            l.pop(-1)
            dfs(result, S, index+1, l)
        list.sort(S)
        result = []
        dfs(result, S, 0, [])

        hash = {}
        i = 0
        while i < len(result):
            l = result[i]
            key = ""
            for j in xrange(-1, 0-len(l)-1, -1):
                key = key + str(l[j]) + "-"
            if key in hash.keys():
                result.pop(i)
            else:
                hash[key] = "x"
                i = i + 1

        return result

if __name__ == "__main__":
    s = Solution()
    one_set = [4,1,0]
    print s.subsetsWithDup(one_set)
