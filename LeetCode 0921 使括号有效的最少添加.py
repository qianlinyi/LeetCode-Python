class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        st = []
        for c in s:
            if len(st) == 0:
                st.append(c)
            else:
                if st[-1] == '(' and c == ')':
                    st.pop()
                else:
                    st.append(c)
        return len(st)
