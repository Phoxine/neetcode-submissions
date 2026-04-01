class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s_length = len(s)
        for i in range(s_length//2):
            tmp = s[i]
            s[i] = s[s_length-1-i]
            s[s_length-1-i] = tmp