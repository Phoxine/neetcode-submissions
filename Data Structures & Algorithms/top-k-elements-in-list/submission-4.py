class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_arr = [None] * len(nums)
        f_dict = {}
        for num in nums:
            if num not in f_dict:
                f_dict[num] = 1
            else:
                f_dict[num] += 1
        
        tmp_arr = []
        for key, value in f_dict.items():
            if count_arr[value-1] is None:
                count_arr[value-1] = [key]
            else:
                count_arr[value-1].append(key)
        for i in range(len(count_arr) -1, -1, -1):
            if count_arr[i] is not None and len(tmp_arr) != k:
                for item in count_arr[i]:
                    tmp_arr.append(item)

        return tmp_arr