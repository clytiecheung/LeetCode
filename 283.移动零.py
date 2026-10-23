class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        slow = 0
        for fast in range(len(nums)):
            if nums[fast] != 0:
                if fast != slow:
                    nums[fast], nums[slow] = nums[slow], nums[fast]
                slow += 1
            