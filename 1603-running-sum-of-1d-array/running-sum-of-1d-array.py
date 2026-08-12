class Solution(object):
    def runningSum(self, nums):
        s = 0
        for i in range(len(nums)):
            nums[i] = nums[i] + s
            s = nums[i]
        return nums
            
        