class Solution:
    def calPoints(self, operations: list[str]) -> int:
        st = []
        for i in operations:
            if i == "+":
                st.append(st[-1]+st[-2])
            elif i == 'D':
                st.append(st[-1]*2)
            elif i == 'C':
                st.pop()
            else:
                st.append(int(i))
        return sum(st)