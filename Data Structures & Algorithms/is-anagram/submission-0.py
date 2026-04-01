class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_dict = {}
        for i in range(len(s)):
            if s[i] not in s_dict:
                s_dict[s[i]] = 1
            else:
                s_dict[s[i]] += 1
        for i in range(len(t)):
            if t[i] not in s_dict:
                return False
            else:
                if s_dict[t[i]] > 1:
                    s_dict[t[i]] -= 1
                else:
                    s_dict.pop(t[i], None)
        if not s_dict:
            return True
        return False