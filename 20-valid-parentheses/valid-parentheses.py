class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        open_b = "([{"
        close_b = ")]}"
        d = dict(zip(close_b,open_b))
        for i in range(len(s)):
            if s[i] == '(' or s[i] == '{' or s[i] == '[':
                st.append(s[i])
            else:
                if not st:
                    return False
                else:
                    if d[s[i]] == st[-1]:
                        st.pop()
                    else:
                        return False
        if not st:
            return True
        else:
            return False