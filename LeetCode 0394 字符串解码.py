class Solution:
    def decodeString(self, s: str) -> str:
        st = []
        for c in s:
            if c == ']':
                res = ''
                while len(st) and st[-1] != '[':
                    res = st[-1] + res
                    st.pop()
                st.pop()
                num = ''
                while len(st) and st[-1].isdigit():
                    num = st[-1] + num
                    st.pop()
                for _ in range(int(num)):
                    st.append(res)
            else:
                st.append(c)
        return ''.join(st)