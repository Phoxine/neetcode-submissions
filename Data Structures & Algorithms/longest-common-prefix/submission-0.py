class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        for i in range(len(strs[0])):
            for index in range(1, len(strs)):
                if i == len(strs[index]) or strs[index][i] != strs[0][i]:
                    return strs[0][:i]
        
        return strs[0]
