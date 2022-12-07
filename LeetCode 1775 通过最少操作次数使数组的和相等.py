class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        def help(h1: List[int], h2: List[int], diff: int) -> int:
            h = [0] * 7
            for i in range(1, 7):
                h[6 - i] += h1[i]
                h[i - 1] += h2[i]
            res = 0
            for i in range(5, 0, -1):
                if diff <= 0:
                    break
                t = min((diff + i - 1) // i, h[i])
                res += t
                diff -= t * i
            return res

        n, m = len(nums1), len(nums2)
        if 6 * n < m or 6 * m < n:
            return -1
        cnt1 = [0] * 7
        cnt2 = [0] * 7
        diff = 0
        for i in nums1:
            cnt1[i] += 1
            diff += i
        for i in nums2:
            cnt2[i] += 1
            diff -= i
        if diff == 0:
            return 0
        if diff > 0:
            return help(cnt2, cnt1, diff)
        return help(cnt1, cnt2, -diff)
