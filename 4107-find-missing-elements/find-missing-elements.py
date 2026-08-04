class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        mx = max(nums)
        mn = min(nums)
        n = []
        for i in range(mn,mx+1):
            if i not in nums:
                n.append(i)
        return n