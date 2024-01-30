class Solution:
    def square(row: int, column: int) -> int:
        pass

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        squares = [{} for i in range(9)]
        rows = [{} for i in range(9)]
        columns = [{} for i in range(9)]
        if len(board) != 9 and len(board[0]) != 9:
            return False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if(board[i][j]=='.'):
                    continue
                square = 0
                row = i
                column = j
                if row <= 2 and column <= 2:
                    square = 0
                elif row <= 2 and column <= 5:
                    square = 1
                elif row <= 2 and column <= 8:
                    square = 2
                elif row <= 5 and column <= 2:
                    square = 3
                elif row <= 5 and column <= 5:
                    square = 4
                elif row <= 5 and column <= 8:
                    square = 5
                elif row <= 8 and column <= 2:
                    square = 6
                elif row <= 8 and column <= 5:
                    square = 7
                elif row <= 8 and column <= 8:
                    square = 8
                if (
                    board[i][j] in rows[i]
                    or board[i][j] in columns[j]
                    or board[i][j] in squares[square]
                ):
                    # print(str(i)+' '+str(j))
                    # print('Row'+str(board[i][j] in rows[i]))
                    # print('Column: '+str(board[i][j] in columns[i]))
                    # print('square: '+str(board[i][j] in squares[square]))
                    return False
                else:
                    rows[i][board[i][j]] = 1
                    columns[j][board[i][j]] = 1
                    squares[square][board[i][j]] = 1
        return True
