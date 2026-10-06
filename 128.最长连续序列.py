class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        current_nums = set(nums)
        longest = 0
        for num in nums:
            if num - 1 not in current_nums:
                current_num = num
                current_streak = 1
                while current_num + 1 in current_nums:
                    current_num += 1
                    current_streak += 1
                longest = max(longest , current_streak)
        return longest