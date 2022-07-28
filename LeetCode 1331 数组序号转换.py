from typing import List


class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        arr_new = sorted(arr)
        index, dic, ans = 1, {}, []
        for _ in arr_new:
            if _ not in dic:
                dic[_] = index
                index += 1
        for _ in arr:
            ans.append(dic[_])
        return ans
