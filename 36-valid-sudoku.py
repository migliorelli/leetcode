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
            for col_idx in range(9):
                sqr = boxes[row_idx // 3][col_idx // 3]
                if board[row_idx][col_idx] == ".":
                    continue
                if board[row_idx][col_idx] in sqr:
                    return False
                sqr.append(board[row_idx][col_idx])

        return True