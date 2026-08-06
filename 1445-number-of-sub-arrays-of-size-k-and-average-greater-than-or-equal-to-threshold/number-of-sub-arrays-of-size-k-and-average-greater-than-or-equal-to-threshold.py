class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        fw = arr[:k]
        s = sum(fw)
        c = 0
        if s/k >= threshold:
            c += 1
        for i in range(k,len(arr)):
            s = s + arr[i] - arr[i-k]
            if s/k >= threshold:
                c += 1
        return c