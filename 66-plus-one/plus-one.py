class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        d = 0
        for i in range(len(digits)):
            d = d*10 + digits[i]
        d = d + 1
        res = []
        while d:
            res.append(d%10)
            d = d//10
        return res[::-1]

