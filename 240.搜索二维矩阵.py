class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # 从右上角的元素找 （行最大，列最小）
        m = len(matrix)
        n = len(matrix[0])
        row = 0
        col = n - 1
        while row < m and col >= 0:
            current = matrix[row][col]
            if current == target:
                return True
            elif current > target:
                col -=1
            elif current < target:
                row += 1
        return False