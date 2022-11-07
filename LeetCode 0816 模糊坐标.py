from typing import List


class Solution:
    def ambiguousCoordinates(self, s: str) -> List[str]:
        def getDecimal(number: str) -> List[str]:
            n = len(number)
            ans = []
            for i in range(1, n):
                flag = True
                # 多余零判断
                if (number[:i][0] == '0' and len(number[:i]) > 1) or number[i:n].count('0') == len(number[i:n]) or (
                        number[i:n][-1] == '0' and len(number[i:n]) > 1):
                    flag = False
                if flag is True:
                    ans.append(f'{number[:i]}.{number[i:n]}')
            return ans

        ans = []
        s = s[1:-1]
        n = len(s)
        for i in range(1, n):
            l, r = s[:i], s[i:n]
            l_ans, r_ans = getDecimal(l), getDecimal(r)
            if not (l[0] == '0' and len(l) > 1):
                l_ans.append(l)
            if not (r[0] == '0' and len(r) > 1):
                r_ans.append(r)
            for ld in l_ans:
                for rd in r_ans:
                    ans.append(f'({ld}, {rd})')
        return ans
