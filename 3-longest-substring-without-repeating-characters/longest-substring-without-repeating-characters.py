class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        maxlength = 0
        d = set()
        for right in range(len(s)):
            while s[right] in d:
                d.remove(s[left])
                left += 1
            d.add(s[right])
            maxlength = max(maxlength,right-left+1)
        return maxlength