def canEat(piles,hours_have,k):
    hours_needed = 0
    for pile in piles:
        hours_needed += math.ceil(pile/k)
    return hours_needed <= hours_have

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)
        while low < high:
            mid = (low+high)//2
            if canEat(piles,h,mid):
                high = mid
            else:
                low = mid + 1
        return low