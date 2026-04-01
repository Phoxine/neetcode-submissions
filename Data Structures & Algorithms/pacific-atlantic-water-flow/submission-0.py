class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific_set = set()
        atlantic_set = set()
        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        rows = len(heights)
        cols = len(heights[0])
        
        def dfs(x, y, visited):
            visited.add((x, y))
            for dx, dy in directions:
                nx, ny = x+dx, y+dy
                if 0<=nx<rows and 0<=ny<cols and (nx, ny) not in visited and heights[x][y] <= heights[nx][ny]:
                    dfs(nx, ny, visited)
                    
                
        # start with edge of island
        # left side
        for i in range(rows):
            dfs(i, 0, pacific_set)
        # top side
        for j in range(cols):
            dfs(0, j, pacific_set)
        # right side
        for k in range(rows):
            dfs(k, cols-1, atlantic_set)
        # down side
        for l in range(cols):
            dfs(rows-1, l, atlantic_set)


        return list(map(list, pacific_set & atlantic_set))