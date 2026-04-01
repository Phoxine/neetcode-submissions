import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        replace_s = re.sub(r'[^A-Za-z0-9]', '', s.lower())
        s_length = len(replace_s)
        mid_index = s_length // 2
        ignore = s_length % 2 == 1
        tmp_arr = []
        # print(replace_s, mid_index, ignore)
        for i in range(len(replace_s)):
            if i < mid_index:
                tmp_arr.append(replace_s[i])
            elif i == mid_index and ignore:
                continue
            elif i >= mid_index:  
                if not replace_s[i] == tmp_arr.pop() :
                    return False
        # print(tmp_arr)
        return True if not tmp_arr else False