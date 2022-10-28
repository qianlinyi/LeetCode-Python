from typing import List


class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        n = len(arr)
        mod = 10 ** 9 + 7
        st = []
        left, right = [0 for _ in range(n)], [0 for _ in range(n)]
        for i in range(n):
            while st and arr[i] <= arr[st[-1]]:
                st.pop()
            left[i] = i - (st[-1] if st else -1)
            st.append(i)
        st.clear()
        for i in range(n - 1, -1, -1):
            while st and arr[i] < arr[st[-1]]:
                st.pop()
            right[i] = (st[-1] if st else n) - i
            st.append(i)
        return sum([arr[i] * left[i] * right[i] for i in range(n)]) % mod
