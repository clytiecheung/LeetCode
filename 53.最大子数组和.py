class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        # current_max = nums[0]
        # best =nums[0]
        # for i in range(1, len(nums)):
        #     current_max = max(current_max + nums[i], nums[i])
        #     best = max(current_max, best)
        # return best
        n = 0
        ans = -inf
        for num in nums:
            if n < 0:
                n = 0
            n += num
            ans = max(n, ans)
        return ans

        