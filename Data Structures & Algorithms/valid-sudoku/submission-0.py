class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        rows = len(board)
        cols = len(board[0])
        
        rows_check = [set() for _ in range(9)]
        cols_check = [set() for _ in range(9)]
        squad_check = [set()for _ in range(9)]

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == '.':
                    continue
                #check cols
                if board[i][j] in cols_check[j]:
                    # print(i, j)
                    # print(board[i][j], cols_check[j])
                    return False
                else:
                    cols_check[j].add(board[i][j])
                #check rows
                if board[i][j] in rows_check[i]:
                    # print(i, j)
                    # print(board[i][j], rows_check[j])
                    return False
                else:
                    rows_check[i].add(board[i][j])
                #check squad
                row_i = i//3
                row_j = j//3
                if board[i][j] in squad_check[row_i*3+row_j]:
                    # print(i, j)
                    # print(row_i, row_j)
                    # print(board[i][j], squad_check[row_i*3+row_j])
                    return False
                else:
                    squad_check[row_i*3+row_j].add(board[i][j])
        return True
