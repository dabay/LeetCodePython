# -*- coding: utf8 -*-
'''
Given a string containing only digits, restore it by returning all possible valid IP address combinations.

For example:
Given "25525511135",

return ["255.255.11.135", "255.255.111.35"]. (Order does not matter)

又是如此冗长的代码，下提交吧，下次再改进~
'''

class Solution:
    # @param s, a string
    # @return a list of strings
    def restoreIpAddresses(self, s):
        def fill_candidate_list(candiate_list, string, index=0, var_list=[], left_dot=3):
            if index > len(string)-1:
                return
            if left_dot == 0:
                if string[index] == "0":
                    if index == len(string) -1 :
                        var_list.append("0")
                        candidate_list.append(list(var_list))
                        var_list.pop(-1)
                    return
                if len(string[index:]) <= 3 and index<len(string):
                    var_list.append(string[index:])
                    candidate_list.append(list(var_list))
                    var_list.pop(-1)
                    return
            if string[index] == "0":
                var_list.append(string[index])
                fill_candidate_list(candidate_list, string, index+1, var_list, left_dot-1)
                var_list.pop(-1)
            else:
                for i in xrange(1,4):
                    var_list.append(string[index:index+i])
                    fill_candidate_list(candidate_list, string, index+i, var_list, left_dot-1)
                    var_list.pop(-1)

        def refine_candidate_list(candidate_list):
            refined_list = []
            i = 0
            while i<len(candidate_list):
                candidate_ip = candidate_list[i]
                incorrect_ip = False
                ip = []
                for num in candidate_ip:
                    if int(num) > 255:
                        incorrect_ip = True
                        break
                    ip.append(str(int(num)))
                if incorrect_ip is True:
                    candidate_list.pop(i)
                    continue
                else:
                    refined_list.append(".".join(ip))
                    i = i + 1
                    continue
            return refined_list

        def delete_duplicate_ip(ip_list):
            unique_ip_list = []
            for ip in ip_list:
                if ip not in unique_ip_list:
                    unique_ip_list.append(ip)
            return unique_ip_list

        if len(s) > 12:
            return []

        candidate_list = []
        fill_candidate_list(candidate_list, s)
        #print candidate_list
        ip_list = refine_candidate_list(candidate_list)
        #return candidate_list
        return delete_duplicate_ip(ip_list)



if __name__ == "__main__":
    s = Solution()
    print s.restoreIpAddresses("1212121212")