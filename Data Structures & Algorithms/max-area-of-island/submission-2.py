class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
                    # right, down, left,  up
        directions = [(0,1),(1,0),(0,-1),(-1,0)]

        row = len(grid)
        col = len(grid[0])
        # handled_area = set()
        def dfs(x, y):

            # out of range
            if x < 0 or x >= row or y < 0 or y >= col:
                return 0

            # water
            if grid[x][y] == 0:
                return 0

            # already visited
            # if (x,y) in handled_area:
            #     return 0

            # set as visited
            grid[x][y] = 0

            # handled_area.add((x, y))
            result = 1
            for a, b in directions:
                result += dfs(x+a, y+b)
            return result

        max_area = 0
        for i in range(row):
            for j in range(col):
                # start with land
                # if grid[i][j] == 1 and (i,j) not in handled_area:
                if grid[i][j] == 1:
                    max_area = max(max_area, dfs(i,j))

        return max_area