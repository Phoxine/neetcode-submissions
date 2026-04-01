from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        # directions of fruit rotten
        directions = [(0,1), (1,0), (0,-1), (-1,0)]
        queue = deque()
        # to check fresh fruit remained
        fresh_fruit_count = 0
        time = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    fresh_fruit_count += 1
                elif grid[i][j] == 2:
                    queue.append((i,j))
        while fresh_fruit_count > 0 and queue:
            
            # rotten fruit count in current minute
            rotten_count = len(queue)
            # fruit rotten in same minute
            for i in range(rotten_count):
                # rotten fruit position
                rfx, rfy = queue.popleft()

                for dx, dy in directions:
                    nx, ny = rfx+dx, rfy+dy
                    if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 1:
                        # become rotten
                        grid[nx][ny] = 2
                        fresh_fruit_count -= 1
                        # start position to spread at next minute
                        queue.append((nx, ny))
            time += 1

        return -1 if fresh_fruit_count > 0 else time