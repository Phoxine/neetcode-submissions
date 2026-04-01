class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total = 0
        has_zero = False
        for num in nums:
            if num != 0:
                if total == 0:
                    total = 1
                total *= num
            else:
                if has_zero:
                    return [0] * len(nums)
                has_zero = True
                
        result = [1] * len(nums)
        for i in range(len(result)):
            if has_zero:
                result[i] = total if nums[i] == 0 else 0
            else:
                result[i] = total // nums[i]

        return result