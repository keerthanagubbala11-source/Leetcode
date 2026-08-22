class Solution:
    def checkDivisibility(self, n: int) -> bool:
        t = n
        s = 0
        p = 1
        while n != 0:
            a= n % 10
            s += a
            p *= a
            n = n // 10
        r = s+p
        return t % r== 0