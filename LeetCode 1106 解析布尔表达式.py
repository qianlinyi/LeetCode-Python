class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        st = []
        for c in expression:
            if c == ',':
                continue
            if c != ')':
                st.append(c)
                continue
            t = f = 0
            while st[-1] != '(':
                if st.pop() == 't':
                    t += 1
                else:
                    f += 1
            st.pop()
            op = st.pop()
            if op == '|':
                st.append('t' if t else 'f')
            elif op == '&':
                st.append('f' if f else 't')
            else:
                st.append('t' if f else 'f')
        return st[-1] == 't'
