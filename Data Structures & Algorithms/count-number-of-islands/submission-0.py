class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
                    # right, down, left,  up
        directions = [(0,1),(1,0),(0,-1),(-1,0)]

        row = len(grid)
        col = len(grid[0])
        handled_area = set()
        def dfs(x, y):

            # out of range
            if x < 0 or x >= row or y < 0 or y >= col:
                return 0

            # water
            if grid[x][y] == "0":
                return 0

            # already visited
            if (x,y) in handled_area:
                return 0

            handled_area.add((x, y))
            
            for a, b in directions:
                dfs(x+a, y+b)
            return 1

        island_count = 0
        for i in range(row):
            for j in range(col):
                # start with land
                if grid[i][j] == "1" and (i,j) not in handled_area:
                    dfs(i,j)
                    island_count += 1

        return island_count