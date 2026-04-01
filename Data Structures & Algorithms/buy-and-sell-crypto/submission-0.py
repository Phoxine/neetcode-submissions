class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        length = len(prices)
        left = 0
        right = 0
        max_profit = 0
        for right in range(length):
            if prices[left] < prices[right]:
                max_profit = max(max_profit, prices[right] - prices[left])
            else:
                left = right
        
        return max_profit
            