class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefix = [0]
        n = len(nums)
        s = 0
        for i in range(n):
            s = s + nums[i]
            prefix.append(s)
        print(prefix)
        right = 0
        left = 0
        for i in range(len(prefix)-1):
            left = prefix[i]
            right = prefix[n] - prefix[i+1]
            if left == right:
                return i
        return -1