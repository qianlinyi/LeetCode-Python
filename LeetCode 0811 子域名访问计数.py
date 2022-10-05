from collections import Counter
from typing import List


class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        cnt = Counter()
        for cpdomain in cpdomains:
            num, domain = cpdomain.split(' ')
            domain = '.' + domain
            s = ''
            for i, c in enumerate(domain[::-1]):
                s = c + s
                if c == '.':
                    cnt[s] += int(num)
        ans = [f'{value} {key[1:]}' for key, value in cnt.items()]
        return ans
