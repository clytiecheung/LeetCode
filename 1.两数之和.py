class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hashmap={}
        for i, num in enumerate(nums):
            key = target - num
            if key in hashmap:
                return [hashmap[key], i]
            hashmap[num] = i
        return []