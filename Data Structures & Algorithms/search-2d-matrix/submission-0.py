class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        target_row = -1

        for i in range(len(matrix)):
            if matrix[i][0] <= target <= matrix[i][-1]:
                if target == matrix[i][0] or target == matrix[i][-1]:
                    return True
                else:
                    target_row = i
        if target_row == -1:
            return False
        
        target_array = matrix[target_row]
        array_length = len(matrix[target_row])
        l, m, r = 0, array_length // 2, array_length - 1
        
        while True:
            if target_array[m] == target:
                return True
            else:
                if target > target_array[m]:
                    l = m
                elif target < target_array[m]:
                    r = m
                if r-l == 1:
                    return False
                m = (r - l) // 2
            
