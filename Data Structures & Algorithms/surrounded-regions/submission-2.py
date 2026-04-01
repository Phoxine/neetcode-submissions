class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows = len(board)
        cols = len(board[0])
        
        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        # start with edge, change all nearby 'O' to 'S'
        def dfs(x, y):
            # skip out of range or X or S (safe)
            if x < 0 or x >=rows or y < 0 or y >= cols or board[x][y] != 'O':
                return
            board[x][y] = 'S'
            for dx, dy in directions:
                dfs(x+dx, y+dy)
        
        
        
        for i in range(rows):
            # left edge
            dfs(i, 0)
            # right edge
            dfs(i, cols-1)
        for j in range(cols):
            # top edge
            dfs(0, j)
            dfs(rows-1, j)

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 'S':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'