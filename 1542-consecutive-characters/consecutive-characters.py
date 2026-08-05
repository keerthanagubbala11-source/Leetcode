class Solution:
    def maxPower(self, s: str) -> int:
        c = 1
        mx = 0
        for i in range(1,len(s)):
            if s[i] == s[i-1]:
                c += 1
            else:
                mx = max(c,mx)
                c = 1
        return max(mx,c)