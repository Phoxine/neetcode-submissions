class Solution:
    def rob(self, nums: List[int]) -> int:
        
        dp = [-1] * len(nums)

        def dfs(i):
            # no more house to rob
            if i>=len(nums):
                return 0
            if dp[i] != -1:
                return dp[i]
            # go to next house, or current house and one more next house
            dp[i] = max(dfs(i+1), nums[i] + dfs(i+2))
            return dp[i]
        return dfs(0)