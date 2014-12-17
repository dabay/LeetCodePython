# -*- coding: utf8 -*-
'''
Given an absolute path for a file (Unix-style), simplify it.

For example,
path = "/home/", => "/home"
path = "/a/./b/../../c/", => "/c"

Corner Cases:
Did you consider the case where path = "/../"?
In this case, you should return "/".
Another corner case is the path might contain multiple slashes '/' together, such as "/home//foo/".
In this case, you should ignore redundant slashes and return "/home/foo".
'''

class Solution:
    # @param path, a string
    # @return a string
    def simplifyPath(self, path):
        folder_list = path.split("/")[1:]
        folder_stack = []
        for f in folder_list:
            if f == "":
                continue
            elif f == ".":
                continue
            elif f == "..":
                if len(folder_stack) == 0:
                    continue
                else:
                    folder_stack.pop(-1)
            else:
                folder_stack.append(f)

        if len(folder_stack) == 0:
            return "/"

        folder_string = ""
        for f in folder_stack:
            folder_string = folder_string + "/" + f
        return folder_string


if __name__ == "__main__":
    s = Solution()
    print s.simplifyPath("/.")



  
