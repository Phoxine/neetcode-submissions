class Solution:
    def findMin(self, nums: List[int]) -> int:

        # num[l] must bigger than num[r] if rotate_time % len(nums) > 0 

        l, r = 0 , len(nums) - 1
        result = nums[0]
        
        while l <= r:
            if nums[l] < nums[r]:
                result = min(result, nums[l])
                break
            mid = (l+r) // 2
            result = min(result, nums[mid])
            if nums[mid] >= nums[l]:
                l = mid + 1
            elif nums[mid] < nums[l]:
                r = mid - 1

        return result