class Solution:
    def climbStairs(self, n: int) -> int:

        tmp_arr = [0] * (n+1)
        tmp_arr[0] = 1
        tmp_arr[1] = 2
        for i in range(2, n, 1):
            tmp_arr[i] = tmp_arr[i-2] + tmp_arr[i-1]
        print(tmp_arr)
        return tmp_arr[n-1]
        
        