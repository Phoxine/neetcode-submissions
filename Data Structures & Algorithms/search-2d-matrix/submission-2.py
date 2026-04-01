class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        target_row = -1

        top, bottom = 0, len(matrix) - 1
        if target <= matrix[top][-1]:
            target_row = top
        elif target >= matrix[bottom][0]:
            target_row = bottom
        else:
            while top <= bottom:
                mid = (top + bottom) // 2 
                if matrix[mid][0] <= target <= matrix[mid][-1]:
                    target_row = mid
                    break
                elif target > matrix[mid][-1]:
                    top = mid + 1
                else:
                    bottom = mid - 1
        if target_row == -1:
            return False
        target_array = matrix[target_row]
        l,  r = 0, len(matrix[target_row]) - 1
        while l <= r:
            m = (l + r) // 2
            if target_array[m] == target:
                return True
            else:
                if target > target_array[m]:
                    l = m + 1
                elif target < target_array[m]:
                    r = m - 1
        return False
