from collections import deque


class Solution:
    def reformatNumber(self, number: str) -> str:
        d = deque()
        for c in number:
            if c.isdigit():
                d.append(c)
        ans = ''
        while len(d) > 4:
            for _ in range(3):
                ans += d[0]
                d.popleft()
            ans += '-'
        if len(d) == 4:
            for _ in range(2):
                for _ in range(2):
                    ans += d[0]
                    d.popleft()
                ans += '-'
        else:
            while len(d) > 0:
                ans += d[0]
                d.popleft()
            ans += '-'
        ans = ans[:-1]
        return ans
