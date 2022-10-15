from collections import deque
from typing import List


class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        index = 1
        st = deque()
        ans = []
        target = deque(target)
        while index <= n and target:
            st.append(index)
            ans.append('Push')
            if st[0] != target[0]:
                st.popleft()
                ans.append('Pop')
            else:
                st.popleft()
                target.popleft()
            index += 1
        return ans
