class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def sumRange(self, left: int, right: int) -> int:
        prefix = list(itertools.accumulate(self.nums))
        s = 0
        if left != 0:
            s = prefix[right] - prefix[left-1]
        else:
            s = prefix[right]
        return s


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)