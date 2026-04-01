class Solution:
    def validPalindrome(self, s: str) -> bool:
        if len(s) < 3:
            return True
        l, r = 0, len(s) - 1

        def delete_and_check(l, r):
            while l < r:
                if s[l] == s[r]:
                    l += 1
                    r -= 1
                else:
                    return False
            return True
            
        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                return delete_and_check(l+1, r) or delete_and_check(l, r-1)

        return True