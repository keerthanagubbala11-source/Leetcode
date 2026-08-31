def sum_d(n):
    s = 0
    while n != 0:
        a = n % 10
        s = s + a**2
        n = n // 10
    return s
class Solution(object):
    def isHappy(self, n):
        while True:
            if n < 10:
                break
            n = sum_d(n)
        if n == 1 or n == 7:
            return True
        else:
            return False