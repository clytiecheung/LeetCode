from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # 解法一
        # n, m = len(s), len(p)
        # if n < m:
        #     return []
        # res = []
        # p_count = [0]*26
        # s_count = [0]*26
        # for i in range(m):
        #     s_count[ord(s[i]) - ord('a')] += 1
        #     p_count[ord(p[i]) - ord('a')] += 1
        # if s_count == p_count:
        #     res.append(0)
        # for i in range(m, n):
        #     s_count[ord(s[i]) - ord('a')] += 1
        #     s_count[ord(s[i - m]) - ord('a')] -= 1
        #     if s_count == p_count:
        #         res.append(i - m + 1)
        # return res

        # 解法二
        n, m = len(s), len(p)
        if m > n:
            return []
        s_count = Counter(s[:m])
        p_count = Counter(p)
        res = []
        if s_count == p_count:
            res.append(0)
        for i in range(m, n):
            s_count[s[i]] += 1
            s_count[s[i - m]] -= 1
            if s_count[s[i - m]] == 0:
                del s_count[s[i - m]]

            if s_count == p_count:
                res.append(i - m + 1)
        return res