class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        if len(nums) < 3:
            return []
        nums.sort()
        ans = []
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            if nums[i] > 0:
                break
            left = i + 1
            right = len(nums) - 1
            while left < right: #注意双指针的循环判定边界
                total = nums[i] + nums[left] + nums[right]
                if total == 0:
                    ans.append([nums[i], nums[left], nums[right]])
                     # 找到答案后，左右指针都要移动
                    left += 1
                    right -=1

                      # 左指针去重：跳过与当前 left 相同的元素
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    # 右指针去重：跳过与当前 right 相同的元素
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif total > 0:# 和大于0，右指针左移，使数字变小
                    right -= 1
                elif total < 0:# 和小于0，左指针右移，使数字变大
                    left += 1 
        return ans