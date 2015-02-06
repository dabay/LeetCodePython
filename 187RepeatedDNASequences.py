# -*- coding: utf8 -*-
'''
__author__ = 'dabay.wang@gmail.com'

187: Repeated DNA Sequences
https://oj.leetcode.com/problems/repeated-dna-sequences/

All DNA is composed of a series of nucleotides abbreviated as A, C, G, and T, for example: "ACGAATTCCG".
When studying DNA, it is sometimes useful to identify repeated sequences within the DNA.
Write a function to find all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule.

For example,
Given s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT",
Return:
["AAAAACCCCC", "CCCCCAAAAA"].

===Comments by Dabay===
如果使用双重循序，结果会超时。
建立一个hash表，用key来记录每一个需要比较的字符串，用value来记录出现的次数。
一样一次遍历就可以了。
最后在遍历一次hash表，把重复出现的字符串放到结果中。
'''

class Solution:
    # @param s, a string
    # @return a list of strings
    def findRepeatedDnaSequences(self, s):
        res = []
        sequence_dict = {}
        i = 0
        while i < len(s) - 9:
            compare_string = s[i:i+10]
            if compare_string not in sequence_dict:
                sequence_dict[compare_string] = 1
            else:
                sequence_dict[compare_string] += 1
            i += 1
        for key in sequence_dict:
            if sequence_dict[key] > 1:
                res.append(key)
        return res


def main():
    sol = Solution()
    s = "CCAAGTCTAAAAGAACGATCACTCCGCGCCACCCCGGGTTACGCACCTCACGTTGAGTGAGGAGATGGCCAAGTCTAAAAA"
    print sol.findRepeatedDnaSequences(s)


if __name__ == "__main__":
    import time
    start = time.clock()
    main()
    print "%s sec" % (time.clock() - start)




