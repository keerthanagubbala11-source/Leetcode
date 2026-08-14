class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        csum = 0
        subcn = 0
        seen ={0:1}
        for i in nums:
            csum += i
            req = csum - k
            if req in seen:
                subcn += seen[req]
            seen[csum] = seen.get(csum,0) + 1
        return subcn