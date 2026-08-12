class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        s = 0
        res = []
        for i in range(len(nums)):
                s += nums[i]
                res.append(s)
        return res