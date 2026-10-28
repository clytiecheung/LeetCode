class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        if not matrix:
            return []
        res = []
        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1
        while True:
            for i in range(left, right + 1):
                res.append(matrix[top][i])
            top += 1
            if top > bottom: break

            for j in range(top, bottom + 1):
                res.append(matrix[j][right])
            right -= 1
            if right < left: break

            for i in range(right, left - 1, -1):
                res.append(matrix[bottom][i])
            bottom -= 1
            if bottom < top: break

            for j in range(bottom, top - 1, -1):
                res.append(matrix[j][left])
            left += 1
            if left > right: break

        return res
