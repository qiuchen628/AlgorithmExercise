class Solutin(object):
    def maximalSquare(self, matrix):
        """
        :param matrix:
        :return: int
        """
        if not matrix:
            return 0
        row, col = len(matrix), len(matrix[0])
        table, curr_max = [[0] * col for _ in range(row)], 0
        for i in range(0, row):
            for j in range(0, col):
                if i == 0:
                    table[0][j] = int(matrix[0][j])
