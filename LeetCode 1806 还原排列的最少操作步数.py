class Solution:
    def reinitializePermutation(self, n: int) -> int:
        perm = [_ for _ in range(n)]
        arr = [perm[i // 2] if i % 2 == 0 else perm[n // 2 + (i - 1) // 2] for i, _ in enumerate(perm)]
        ans = 1
        while arr != perm:
            temp = [arr[i // 2] if i % 2 == 0 else arr[n // 2 + (i - 1) // 2] for i, _ in enumerate(arr)]
            arr = temp
            ans += 1
        return ans
