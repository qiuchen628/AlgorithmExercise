def searchMatrix(matrix, target):
    m = len(matrix)
    if m == 0:
        return False
    n = len(matrix[0])
    if n == 0:
        return False
    y = m-1
    x = 0
    while x < n and y >= 0:
        if matrix[y][x] == target:
            return True
        elif matrix[y][x] < target:
            x += 1
        else:
            y -= 1
    return False


matrix1 = [[1, 3, 4], [6, 11, 13], [22, 24, 28]]

"""
1  3  4
6  11 13
22 24 28
"""

res = searchMatrix(matrix1, 11)

print("Is the target number is in the matrix? Ans:", res)
