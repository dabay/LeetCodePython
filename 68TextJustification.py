# -*- coding: utf8 -*-
'''
__author__ = 'dabay.wang@gmail.com'

68: Text Justification
https://oj.leetcode.com/problems/text-justification/

Given an array of words and a length L, format the text such that each line has exactly L characters
and is fully (left and right) justified.

You should pack your words in a greedy approach; that is, pack as many words as you can in each line.
Pad extra spaces ' ' when necessary so that each line has exactly L characters.

Extra spaces between words should be distributed as evenly as possible.
If the number of spaces on a line do not divide evenly between words,
the empty slots on the left will be assigned more spaces than the slots on the right.

For the last line of text, it should be left justified and no extra space is inserted between words.

For example,
words: ["This", "is", "an", "example", "of", "text", "justification."]
L: 16.

Return the formatted lines as:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]
Note: Each word is guaranteed not to exceed L in length.

Corner Cases:
A line other than the last line might contain only one word. What should you do in this case?
In this case, that line should be left-justified.

===Comments by Dabay===
感觉不太难...
但是，代码一如既往的冗长...
'''

class Solution:
    # @param words, a list of strings
    # @param L, an integer
    # @return a list of strings
    def fullJustify(self, words, L):
        def fullJustify2(words, length, res):
            if len(words) == 0:
                return
            i = 0
            l = len(words[i])
            i = i + 1
            while l < length:
                if i == len(words):
                    res.append(words)
                    return
                l = l + 1 + len(words[i])
                if l > length:
                    break
                i = i + 1
            res.append(words[:i])
            fullJustify2(words[i:], length, res)

        def list_to_string(res, length):
            def all_length(l):
                length = 0
                for w in l:
                    length = length + len(w)
                return length

            strings = []
            i = 0
            while i < len(res)-1:
                if len(res[i]) == 1:
                    string = res[i][0] + ' ' * (length - len(res[i][0]))
                    strings.append(string)
                    i = i + 1
                    continue
                for j in xrange(1, len(res[i])):
                    res[i][j] = " " + res[i][j]

                k = 1
                while all_length(res[i]) < length:
                    res[i][k] = " " + res[i][k]
                    k = k + 1
                    if k == len(res[i]):
                        k = 1
                string = ''.join(res[i])
                strings.append(string)
                i = i + 1
            # handle last row res[-1]
            last_string = ' '.join(res[-1])
            strings.append(last_string + ' ' * (length - len(last_string)))
            return strings

        res = []
        fullJustify2(words, L, res)
        return list_to_string(res, L)


def main():
    sol = Solution()
    words = ["This", "is", "an", "example", "of", "text", "justification."]
    words = ["What","must","be","shall","be."]
    L = 16
    L = 12
    print sol.fullJustify(words, L)


if __name__ == '__main__':
    import time
    start = time.clock()
    main()
    print "%s sec" % (time.clock() - start)
