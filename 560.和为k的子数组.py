class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        cur_sum = 0
        harsh_map = {0: 1}
        for i in range(0, len(nums)):
            cur_sum += nums[i]
            target = cur_sum - k
            if target in harsh_map:
                count += harsh_map[target]
            harsh_map[cur_sum] = harsh_map.get(cur_sum, 0) + 1

        return count