class Solution:
    def isValid(self, s: str) -> bool:
        tmp_arr = []
        for i in range(len(s)):
            if s[i] == "(":
                tmp_arr.append(")")
            elif s[i] == "{":
                tmp_arr.append("}")
            elif s[i] == "[":
                tmp_arr.append("]")
            elif tmp_arr and s[i] == tmp_arr[-1]:
                tmp_arr.pop()
            else:
                return False
        
        return True if not tmp_arr else False