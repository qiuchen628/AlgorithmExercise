class Solution:
    def isValidSudoku(self, board):
        N = 9
        row = [set() for _ in range(N)]
        col = [set() for _ in range(N)]
        boxes = [set() for _ in range(N)]

        for r in range(N):
            for c in range(N):
                val = board[r][c]
                if val == '.':
                    continue

                if val in row[r]:
                    return False
                row[r].add(val)

                if val in col[c]:
                    return False
                col[c].add(val)

                idx = (r//3) * 3 + c // 3
                if val in boxes[idx]:
                    return False
                boxes[idx].add(val)

        return True

case1 = [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

obj = Solution()
res = obj.isValidSudoku(case1)

print('the result of valid sudoku is: ', res)



