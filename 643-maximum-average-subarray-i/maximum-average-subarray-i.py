class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        mx = -1000000000
        left = 0
        s = 0
        for right in range(len(nums)):
            s += nums[right]
            if right >= k-1:
                avg = s/k
                mx = max(mx,avg)
                s -= nums[left]
                left += 1
        return mx