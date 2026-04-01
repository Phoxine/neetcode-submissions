class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_count = {}
        s2_count = {}
        need = 0
        for c in s1:
            s1_count[c] = 1 + s1_count.get(c, 0)
            need += 1
        
        count = 0
        l = 0
        for r in range(len(s2)):
            if s2[r] in s1_count:
                if s1_count[s2[r]] > s2_count.get(s2[r], 0):
                    count += 1
                s2_count[s2[r]] = 1 + s2_count.get(s2[r], 0)
            else:
                l = r+1
                count = 0
                s2_count = {}

            while count == need:
                if s1_count == s2_count:
                    return True
                else:
                    s2_count[s2[l]] -= 1
                    if s1_count[s2[l]] > s2_count[s2[l]]:
                        count -= 1
                    if s2_count[s2[l]] == 0:
                        del s2_count[s2[l]]
        return False