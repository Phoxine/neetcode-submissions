class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        if s == t:
            return s
        t_count = {}
        s_count = {}
        min_length = float('inf')
        need = 0
        count = 0
        for c in t:
            t_count[c] = 1 + t_count.get(c, 0)
            need += 1
        
        min_l, min_r = -1, -1
        l = 0
        for r in range(len(s)):
            if s[r] in t_count:
                if t_count[s[r]] > s_count.get(s[r], 0):
                    count += 1
                s_count[s[r]] = 1 + s_count.get(s[r], 0)
            
            while need == count:
                if (r-l) <= min_length:
                    min_length = r - l
                    min_l, min_r = l, r
                if s[l] in s_count:
                    s_count[s[l]] -= 1
                    if s_count[s[l]] < t_count[s[l]]:
                        count -= 1
                l += 1

        return "" if min_l == -1 and min_r == -1 else s[min_l:min_r + 1]


