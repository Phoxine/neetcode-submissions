class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = float("-inf")
        current_sum = float("-inf")
        for num in nums:
            if current_sum == float("inf"):
                current_sum = num
            current_sum += num
            if current_sum < 0 or current_sum < num:
                current_sum = num

            max_sum = max(max_sum, current_sum)

        return max_sum