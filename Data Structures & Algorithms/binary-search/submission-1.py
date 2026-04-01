class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1
        if nums[start] == target:
            return start
        if nums[end] == target:
            return end
        mid = len(nums) // 2
        
        count = 0
        while count < 10000:
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                end = mid
                mid = (end - start) // 2 + start 
            elif nums[mid] < target:
                start = mid
                mid = (end -start) // 2 + start

            count += 1
        return -1