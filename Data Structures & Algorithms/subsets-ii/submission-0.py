class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = set()

        def backtrack(subset, index):
            if index == len(nums):
                result.add(tuple(subset))
                return
            subset.append(nums[index])
            # find include current number
            backtrack(subset, index+1)
            # find exculde current number
            subset.pop()
            backtrack(subset, index+1)
        nums.sort()
        backtrack([], 0)
        return [list(r) for r in result]
            