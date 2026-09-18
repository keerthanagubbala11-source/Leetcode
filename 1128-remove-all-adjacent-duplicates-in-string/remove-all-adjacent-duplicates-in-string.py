class Solution:
    def removeDuplicates(self, s: str) -> str:
        st = []
        s = list(s)
        for i in range(len(s)):
            if not st:
                st.append(s[i])
            else:
                if st[-1] == s[i]:
                    st.pop()
                else:
                    st.append(s[i])
        return "".join(st)  