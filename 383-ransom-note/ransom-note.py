class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        m = {}
        for i in magazine:
            if i in m.keys():
                m[i] += 1
            else:
                m[i] = 1
        for i in ransomNote:
            if i not in m.keys():
                return False
            else:
                if m[i] > 0:
                    m[i] -= 1
                else:
                    return False
        return True