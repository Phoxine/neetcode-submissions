class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        tmp_array = set()
        for i in range(len(nums)):
            if not tmp_array:
                tmp_array.add(nums[i])
                continue
            if nums[i] not in tmp_array:
                tmp_array.add(nums[i])
                continue
            return True
        return False
            