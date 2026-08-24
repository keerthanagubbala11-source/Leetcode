class Solution:
    def sumAndMultiply(self, n: int) -> int:
        nums = []
        while n:
            if n % 10 != 0:
                nums.append(n%10)
            n = n // 10
        num = nums[::-1]
        x = 0
        for i in range(len(num)):
            x = x*10 + num[i]
        s = 0
        t = x
        while x:
            s = s + x % 10
            x = x // 10
        return t*s
