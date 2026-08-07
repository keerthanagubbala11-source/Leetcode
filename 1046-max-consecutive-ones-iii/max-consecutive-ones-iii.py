class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        zeroscount = 0
        maxcount = 0
        left = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                zeroscount += 1
            while zeroscount > k:
                if nums[left] == 0:
                    zeroscount -= 1
                left += 1
            maxcount = max(maxcount,right-left+1)
        return maxcount