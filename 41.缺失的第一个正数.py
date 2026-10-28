class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        # 简洁解法 时间复杂度O(NlogN)，不满足题意
        nums.sort()
        ans = 1
        for num in nums:
            if ans == num:
                ans += 1
        return ans

    #    # 正确解法：原地哈希    
    
    #    # 时间复杂度O(N): 不能用排序（O(NlogN)）
    #    # 空间复杂度O(1): 不能新建哈希表记录出现过的数字
    #     n = len(nums)

    #      # 1. 原地交换，把每个数字放到它该在的位置（数字 x 放到索引 x-1 处）
    #     for i in range(n):
    #         # 使用 while 是因为交换过来的新数字可能也需要归位
    #         # 条件解释：当前数字在 [1, n] 范围内，且它不在正确的位置上，且要交换的目标位置上的数字和它不一样（防止死循环）
    #         while 1 <= nums[i]<= n and nums[i] != nums[nums[i] - 1]:
    #             # 把 nums[i] 放到它该去的索引 nums[i]-1 处
    #             # nums[i], nums[nums[i] - 1]=nums[nums[i] - 1], nums[i] 单行交叉赋值会超出时间限制
    #             target_idx = nums[i] - 1
    #             temp = nums[i]
    #             nums[i] = nums[target_idx]
    #             nums[target_idx] = temp

    #     # 2. 再次遍历，寻找第一个不匹配的位置
    #     for i in range(n):
    #         if nums[i] != i + 1:
    #             return i + 1 # 缺失的数字就是当前位置应有的数字
                
    #     # 3. 如果所有位置都匹配（例如 [1,2,3]），说明缺失的是 n+1
    #     return n + 1

            