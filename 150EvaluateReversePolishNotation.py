# -*- coding: utf8 -*-
'''
https://oj.leetcode.com/problems/evaluate-reverse-polish-notation/

Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, /. Each operand may be an integer or another expression.

Some examples:
  ["2", "1", "+", "3", "*"] -> ((2 + 1) * 3) -> 9
  ["4", "13", "5", "/", "+"] -> (4 + (13 / 5)) -> 6
'''
class Solution:
    # @param tokens, a list of string
    # @return an integer
    def evalRPN(self, tokens):
        num_stack = []
        sign_stack = []
        for t in tokens:
            if t == "+":
                opt2 = num_stack.pop()
                opt1 = num_stack.pop()
                result = opt1 + opt2
                num_stack.append(result)
            elif t == "-":
                opt2 = num_stack.pop()
                opt1 = num_stack.pop()
                result = opt1 - opt2
                num_stack.append(result)
            elif t == "*":
                opt2 = num_stack.pop()
                opt1 = num_stack.pop()
                result = opt1 * opt2
                num_stack.append(result)
            elif t == "/":
                opt2 = num_stack.pop()
                opt1 = num_stack.pop()
                result = 0
                if opt1 * opt2 < 0:
                    result = (abs(opt1) / abs(opt2)) * -1
                else:
                    result = opt1 / opt2
                num_stack.append(result)
            else:
                num_stack.append(int(t))
        return num_stack.pop()

def main():
    s = Solution()
    tokens = ["4","13","5","/","+"]
    print s.evalRPN(tokens)


if __name__ == "__main__":
    import time
    start = time.clock()
    main()
    end = time.clock()
    print "%s sec" % (end - start)

