from collections import Counter
from string import ascii_lowercase

# 栈
class Solution:
    def robotWithString(self, s: str) -> str:
        ans = ''
        cnt = Counter(s)
        mn = 0
        st = []
        for c in s:
            cnt[c] -= 1
            while mn < 25 and cnt[ascii_lowercase[mn]] == 0:
                mn += 1
            st.append(c)
            while st and st[-1] <= ascii_lowercase[mn]:
                ans += st.pop()
        return ans
