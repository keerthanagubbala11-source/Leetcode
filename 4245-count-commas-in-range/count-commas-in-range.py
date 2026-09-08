class Solution:
    def countCommas(self, n: int) -> int:
        dc = int(math.log10(n)+1)
        if dc <= 3:
            return 0
        c = 0
        for i in range(1000,n+1):
            c += 1
        return c
