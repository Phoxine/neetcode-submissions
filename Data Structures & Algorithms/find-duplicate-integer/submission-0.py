class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        duplicated = set()
        for num in nums:
            if num in duplicated:
                return num
            duplicated.add(num)

        return -1