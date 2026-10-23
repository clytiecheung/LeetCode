class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_index = {}
        left = 0
        max_len = 0
        for right in range(len(s)):
            char = s[right]
            if char in char_index and left <= char_index[char]:
                left = char_index[char] + 1
            max_len = max(max_len, right - left + 1)
            char_index[char] = right 
        return  max_len