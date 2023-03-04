from typing import List


class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        ans = [[0] * len(mat2[0]) for _ in range(len(mat1))]
        for row_idx, row_ele in enumerate(mat1):
            for element_idx, row_ele in enumerate(row_ele):
                if row_ele:
                    for col_idx, col_ele in enumerate(mat2[element_idx]):
                        ans[row_idx][col_idx] += row_ele * col_ele
        return ans


object1 = Solution()
res = object1.multiply([[1,2],[3,4]], [[5, 6], [7, 8]])

print('the result is:', res)