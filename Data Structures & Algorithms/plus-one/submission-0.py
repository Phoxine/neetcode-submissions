class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        need_incrementing = True
        i = len(digits) - 1
        while need_incrementing and i >= 0:
            digits[i] += 1
            if digits[i] == 10:
                digits[i] = 0
            else:
                need_incrementing = False
            i -= 1

        if need_incrementing:
            digits.insert(0,1)
        return digits