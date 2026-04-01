class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        self.d_index = 0
        self.result = []


        def dfs(r, c):
            self.result.append(matrix[r][c])
            if len(self.result) == len(matrix) * len(matrix[0]):
                return
            
            #visited
            matrix[r][c] = float('-inf')
            while True:
                dx, dy = directions[self.d_index]
                if 0 <= r+dx < len(matrix) and 0 <= c+dy < len(matrix[0]) and matrix[r+dx][c+dy] != float("-inf"):
                    dfs(r+dx, c+dy)
                    break
                self.d_index = (self.d_index+1) % 4
        dfs(0,0)
        return self.result
                
        

