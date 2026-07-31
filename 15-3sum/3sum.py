class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        n = set()
        for i in range(len(nums)):
            left = i+1
            right = len(nums) - 1
            while left < right:
                s = nums[i] + nums[left] + nums[right]
                if s == 0:
                    t = [nums[i],nums[left],nums[right]]
                    n.add(tuple(t))
                    left += 1
                    right -= 1
                elif s > 0:
                    right -= 1
                else:
                    left += 1
        return list(n)