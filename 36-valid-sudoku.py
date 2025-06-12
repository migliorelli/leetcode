class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for row_idx in range(9):
            arr = []
            for col_idx in range(9):
                if board[row_idx][col_idx] == ".":
                    continue
                if board[row_idx][col_idx] in arr:
                    return False
                arr.append(board[row_idx][col_idx])

        for col_idx in range(9):
            arr = []
            for row_idx in range(9):
                if board[row_idx][col_idx] == ".":
                    continue
                if board[row_idx][col_idx] in arr:
                    return False
                arr.append(board[row_idx][col_idx])

        boxes = [
            [[], [], []],
            [[], [], []],
            [[], [], []],
        ]

        for row_idx in range(9):
            row_quo = 0 if row_idx == 0 else row_idx / 3
            box_row_idx = int(row_quo)

            for col_idx in range(9):
                col_quo = 0 if col_idx == 0 else col_idx / 3
                box_col_idx = int(col_quo)

                sqr = boxes[box_row_idx][box_col_idx]
                if board[row_idx][col_idx] == ".":
                    continue
                if board[row_idx][col_idx] in sqr:
                    return False
                sqr.append(board[row_idx][col_idx])

        return True