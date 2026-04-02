class Solution:
    def tribonacci(self, n: int) -> int:
        
        
        dp = [-1]*(n+3)
        dp[0], dp[1], dp[2] = 0, 1, 1
        if n < 3:
            return dp[n]
        def recursive(i):

            if dp[i] != -1:
                return dp[i]
            dp[i] = recursive(i-3) + recursive(i-2) + recursive(i-1)

            return dp[i]



        return recursive(n)