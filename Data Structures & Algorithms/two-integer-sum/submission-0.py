class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        tmp_array = []
        start_index = 0
        end_index = 0
        for i in range(len(nums)):
            if target - nums[i] not in tmp_array:
                tmp_array.append(nums[i])
            else:
                start_index = tmp_array.index(target - nums[i])
                end_index = i
                break
        return [start_index, end_index]
        