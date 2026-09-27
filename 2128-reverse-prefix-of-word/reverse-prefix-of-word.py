class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        c = 0
        for i in range(len(word)):
            if word[i] == ch:
                c = i
                break
        return word[:c+1][::-1] + word[c+1:]