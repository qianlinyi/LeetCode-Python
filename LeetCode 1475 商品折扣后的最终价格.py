from typing import List


class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        n = len(prices)
        ans, st = [0 for _ in range(n)], [0]
        for i in range(n - 1, -1, -1):
            while st and st[-1] > prices[i]:
                st.pop()
            ans[i] = prices[i] - st[-1]
            st.append(prices[i])
        return ans
