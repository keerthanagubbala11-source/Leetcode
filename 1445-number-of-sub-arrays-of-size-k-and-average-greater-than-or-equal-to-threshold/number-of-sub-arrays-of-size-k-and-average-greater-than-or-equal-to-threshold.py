class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        left = 0
        s = 0 
        c = 0
        for right in range(len(arr)):
            s += arr[right]
            if right >= k-1:
                avg = s / k
                if avg >= threshold:
                    c += 1
                s -= arr[left]
                left += 1
        return c