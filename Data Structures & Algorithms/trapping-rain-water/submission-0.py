class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, 1

        total_unit = 0
        tmp_water = 0

        while r < len(height):
            
            tmp_water += max(0, height[l]-height[r])
            if height[r] >= height[l]:
                total_unit += tmp_water
                tmp_water = 0
                l = r
            r += 1

        # handle last unclosed area
        if tmp_water != 0:
            tmp_water = 0
            r = len(height) - 1
            tmp_l = r - 1
            while r > l:
                tmp_water += max(0, height[r] - height[tmp_l])
                if height[tmp_l] >= height[r]:
                    total_unit += tmp_water
                    tmp_water = 0
                    r = tmp_l
                tmp_l -= 1



        return total_unit