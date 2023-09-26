class Solution:
    def maximumSumOfHeights(self, maxHeights: List[int]) -> int:
        n = len(maxHeights)
        suf = [0] * (n + 1)
        st = [n]
        s = 0
        for i in range(n - 1, -1, -1):
            x = maxHeights[i]
            while len(st) > 1 and x <= maxHeights[st[-1]]:
                j = st.pop()
                s -= maxHeights[j] * (st[-1] - j)
            s += x * (st[-1] - i)
            suf[i] = s
            st.append(i)

        ans = s
        st = [-1]
        pre = 0
        for i, x in enumerate(maxHeights):
            while len(st) > 1 and x <= maxHeights[st[-1]]:
                j = st.pop()
                pre -= maxHeights[j] * (j - st[-1])
            pre += x * (i - st[-1])
            ans = max(ans, pre + suf[i + 1])
            st.append(i)
        return ans
