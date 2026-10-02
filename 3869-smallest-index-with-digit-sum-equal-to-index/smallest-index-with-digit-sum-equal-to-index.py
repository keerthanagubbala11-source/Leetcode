class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            s = 0
            while nums[i]:
                a = nums[i] % 10
                s += a
                nums[i] = nums[i] // 10
            if s == i:
                return i
        else:
            return-1