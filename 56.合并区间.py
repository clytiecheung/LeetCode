class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        ans =[]
        intervals.sort(key = lambda x: x[0])
        for k in intervals:
            if  not ans or ans[-1][1] < k[0]:
                ans.append(k)
            else:
                ans[-1][1] = max(ans[-1][1], k[1])
        return ans
