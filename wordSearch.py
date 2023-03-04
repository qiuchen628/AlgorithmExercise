class Solution:

    def exist(self, board, word):
        self.ROWS = len(board)
        self.COLS = len(board[0])
        self.board = board

        if not board:
            return False

        for row in range(self.ROWS):
            for col in range(self.COLS):
                if self.backtrack(row, col, word):
                    return True
        return False

    def backtrack(self, row, col, word):
        if len(word) == 0:
            return True
        if row < 0 or row >= len(word) or col < 0 or col >= len(word):
            return False
        tmp = board[row][col]
        board[][]


test_case = Solution()
result = test_case.exist([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ASA")
print("the result is: ", result)