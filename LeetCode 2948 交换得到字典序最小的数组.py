class Solution:

    def lexicographicallySmallestArray(self, nums: List[int],
                                       limit: int) -> List[int]:
        n = len(nums)
        a = sorted(zip(nums, range(n)))

        ans = [0] * n
        i = 0
        while i < n:
            st = i
            i += 1
            while i < n and a[i][0] - a[i - 1][0] <= limit:
                i += 1
            sub = a[st:i]
            sub_idx = sorted(i for _, i in sub)
            for j, (x, _) in zip(sub_idx, sub):
                ans[j] = x
        return ans
