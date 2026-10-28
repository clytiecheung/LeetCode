class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        # 1. 沿主对角线转置矩阵
        for i in range(n):
            for j in range(i, n):
                # 注意：内层循环 j 从 i 开始即可，避免将元素交换两次（换回原样）
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
         # 2. 每一行左右翻转
        for i in range(n):
             # 只需要遍历半行，将头尾元素对调
            for j in range(n//2):
                matrix[i][j], matrix[i][n - j -1] = matrix[i][n - j - 1], matrix[i][j]
       