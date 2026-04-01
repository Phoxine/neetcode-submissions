class Solution:
    def isHappy(self, n: int) -> bool:
        #slow fast


        slow, fast = n, self.sum_of_squares(n)

        while fast != 1:
            # infinity loop
            if slow == fast:
                return False

            fast = self.sum_of_squares(fast)
            fast = self.sum_of_squares(fast)
            slow = self.sum_of_squares(slow)

        return True
    def sum_of_squares(self, n):
        output = 0
        while n:
            digit = n % 10
            digit = digit ** 2
            output += digit
            n = n // 10
        return output