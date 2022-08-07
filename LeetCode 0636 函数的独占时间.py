from typing import List


# 栈
class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        ans = [0 for _ in range(n)]
        st = []
        for log in logs:
            log = log.split(':')
            idx, sign, timestamp = int(log[0]), log[1], int(log[2])
            if sign == 'start':
                if st:
                    ans[st[-1][0]] += timestamp - st[-1][1]
                    st[-1][1] = timestamp
                st.append([idx, timestamp])
            else:
                i, t = st.pop()
                ans[i] += timestamp - t + 1
                if st:
                    st[-1][1] = timestamp + 1
        return ans
