class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        mc = 0
        n = len(word)
        for i in range(len(sequence)):
            c = 0
            while sequence[i:i+n] == word:
                c += 1
                i += n
            mc = max(c,mc)
        return mc