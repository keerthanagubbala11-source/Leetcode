class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        nums.append(0)
        c = 0
        mx= 0
        for i in range(len(nums)):
            if nums[i] == 1:
                c += 1
            if nums[i] == 0:
                mx = max(mx,c)
                c = 0
        return mx