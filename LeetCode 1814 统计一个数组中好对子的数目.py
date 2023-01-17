from collections import Counter


class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        def rev(num: int) -> int:
            return int(str(num)[::-1])

        ans, cnt, mod = 0, Counter(), 10 ** 9 + 7
        for num in nums:
            rev_num = rev(num)
            ans = (cnt[num - rev_num] + ans) % mod
            cnt[num - rev_num] += 1
        return ans
