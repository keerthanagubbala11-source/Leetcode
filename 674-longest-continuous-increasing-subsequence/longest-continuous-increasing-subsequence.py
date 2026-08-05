class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        c = 1
        mx = 0
        for i in range(len(nums)-1):
            if nums[i] < nums[i+1]:
                c += 1
            else:
                mx = max(mx,c)
                c = 1
        return max(c,mx)