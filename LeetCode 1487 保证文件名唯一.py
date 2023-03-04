from typing import List


class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        ans = []
        index = {}
        for name in names:
            if name not in index:
                index[name] = 1
                ans.append(name)
            else:
                k = index[name]
                while f'{name}({k})' in index:
                    k += 1
                t = f'{name}({k})'
                ans.append(t)
                index[name] = k + 1
                index[t] = 1
        return ans
