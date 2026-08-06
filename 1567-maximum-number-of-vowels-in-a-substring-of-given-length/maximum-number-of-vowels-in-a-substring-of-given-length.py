class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        #compute the number of vowels n first
        #k-size substrig
        fw = s[:k]
        vc = 0
        v = 'aeiou'
        for i in fw:
            if i in v:
                vc += 1
        mx = max(0,vc)
        #sliding window logic
        for i in range(k,len(s)):
            if s[i] in v:#new element 
                vc += 1
            if s[i-k] in v:#leaving element
                vc -= 1
            mx = max(mx,vc)
        return mx