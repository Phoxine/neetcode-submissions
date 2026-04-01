class Solution:
    def jump(self, nums: List[int]) -> int:
        jump_time = 0
        
        cur_end = 0
        farthest = 0
        for i in range(len(nums) - 1):
            farthest = max(farthest, i+nums[i])

            if i == cur_end:
                cur_end = farthest
                jump_time += 1
            
        return jump_time