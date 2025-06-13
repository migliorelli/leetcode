class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        n_rows = len(board)
        n_cols = len(board[0])

        for row in range(n_rows):
            for col in range(n_cols):
                if self.backtrack(board, n_rows, n_cols, row, col, word):
                    return True
        
        return False

    def backtrack(self,board,n_rows,n_cols,row,col,suffix):
        if len(suffix) == 0:
            return True
        
        if (row < 0 or row == n_rows 
        or col < 0 or col == n_cols 
        or board[row][col] != suffix[0]):
            return False

        board[row][col] = "*"

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        for row_offset, col_offset in directions:
            response = self.backtrack(
                board, 
                n_rows, n_cols, 
                row+row_offset, col+col_offset, 
                suffix[1:]
            )

            if response:
                return True

        board[row][col] = suffix[0] 
        return False
