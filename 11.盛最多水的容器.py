class Solution:
    def maxArea(self, height: list[int]) -> int:
        left = 0
        right = len(height) - 1
        ans = 0
        while left < right:
            if height[left] < height[right]:
                area = height[left]*(right - left)
                ans = max(area, ans)
                left += 1
            else:
                area = height[right]*(right - left)
                ans = max(area, ans)
                right -= 1
        return ans