class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        memo = [float("inf")] * (amount + 1)

        memo[0] = 0

        for i in range(1, amount+1):
            for coin in coins:

                if i - coin < 0: # no solution
                    continue

                memo[i] = min(memo[i], memo[i-coin] + 1)

        return -1 if memo[amount] == float("inf") else memo[amount]
