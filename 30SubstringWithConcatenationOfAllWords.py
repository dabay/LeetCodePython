# -*- coding: utf8 -*-
'''
__author__ = 'dabay.wang@gmail.com'
https://oj.leetcode.com/problems/substring-with-concatenation-of-all-words/

You are given a string, S, and a list of words, L, that are all of the same length.
Find all starting indices of substring(s) in S that is a concatenation of each word in L
exactly once and without any intervening characters.

For example, given:
S: "barfoothefoobarman"
L: ["foo", "bar"]

You should return the indices: [0,9].
(order does not matter).

===Comments by Dabay===

生成一个hash表来记录每个词在L中出现的次数。
扫描要检查的字符串S，检查以这个字母开始的 长度为L总长度 的字符串，
如果小词在hash表中，值减一；如果最后每一个hash值都是0，说明正好全部匹配完，加入到结果。
重新初始化hash表，进行下一次检查。
'''

class Solution:
    # @param S, a string
    # @param L, a list of string
    # @return a list of integer
    def findSubstring(self, S, L):
        d = {}
        for x in L:
            if x not in d:
                d[x] = 1
            else:
                d[x] += 1
        res = []
        word_length = len(L[0])
        i = 0
        while i < len(S) - word_length * len(L) + 1:
            j = i
            dd = dict(d)
            while j < i + word_length * len(L):
                word = S[j:j+word_length]
                if word in dd:
                    dd[word] -= 1
                    if dd[word] < 0:
                        break
                else:
                    break
                j += word_length
            else:
                res.append(i)
            i += 1
        return res


def main():
    s = Solution()
    string = "aaa"
    dictionary = ["a", "b"]
    print s.findSubstring(string, dictionary)


if __name__ == "__main__":
    import time
    start = time.clock()
    main()
    print "%s sec" % (time.clock() - start)