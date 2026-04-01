class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [-100] * len(cost)
        def dfs(i):
            # no stair or already reach top
            if i >= len(cost):
                return 0
            if dp[i] != -100:
                return dp[i]
            dp[i] = cost[i] + min(dfs(i+1),dfs(i+2))
            return dp[i]
        # compare with staring with floor 0 and floor 1
        return min(dfs(0), dfs(1))