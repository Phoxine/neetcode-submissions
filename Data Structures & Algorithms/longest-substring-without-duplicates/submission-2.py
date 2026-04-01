class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        unique_set = set()
        length = len(s)
        left = 0
        max_length = 0
        for right in range(length):
            while s[right] in unique_set:
                unique_set.remove(s[left])
                left += 1

            unique_set.add(s[right])
            max_length = max(max_length, right - left + 1)
        return max_length
