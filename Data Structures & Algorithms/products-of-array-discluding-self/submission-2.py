class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * len(nums)
        total = 0
        has_zero = False
        multi_zero = False
        for num in nums:
            if num != 0:
                if total == 0:
                    total = 1
                total *= num
            else:
                if has_zero:
                    multi_zero = True
                has_zero = True
                

        for i in range(len(result)):
            if has_zero:
                if multi_zero:
                    result[i] = 0
                    continue
                result[i] = total if nums[i] == 0 else 0
            else:
                result[i] = total // nums[i]

        return result