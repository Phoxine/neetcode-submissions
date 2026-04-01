class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        tmp = None
        for i in range(len(nums)):
            if tmp is None:
                tmp = nums[i]
            else:
                tmp ^= nums[i]

        return tmp