class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        c = []
        w1 = list(word1)
        w2 = list(word2)
        for i in range(max(len(w1),len(w2))):
            if i < len(w1):
                c.append(w1[i])
            if i < len(w2):
                c.append(w2[i])
        return "".join(c)