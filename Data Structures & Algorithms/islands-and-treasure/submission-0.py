from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows = len(grid)
        cols = len(grid[0])
        # directions to search
        directions = [(0,1), (1,0), (0,-1), (-1,0)]
        INF = 2147483647
        # find all treasure position and set as start point to breadth search
        queue = deque()
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    queue.append((i, j))

        

        # search start with treasure
        while queue:
            sx, sy = queue.popleft()
            for dx, dy in directions:
                nx, ny = sx+dx, sy+dy
                # out of range
                if nx < 0 or nx >= rows or ny < 0 or ny >= cols:
                    continue
                # meet water cell
                elif grid[nx][ny] == -1:
                    continue
                elif grid[nx][ny] == INF:
                    queue.append((nx, ny))
                    # update distance of land to nearby treasure
                    grid[nx][ny] = grid[sx][sy] + 1

