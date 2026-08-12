class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.prefix = list(itertools.accumulate(self.nums,initial = 0))

    def sumRange(self, left: int, right: int) -> int:
        s = self.prefix[right+1] - self.prefix[left]
        return s


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)