class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        cnt = Counter([0])
        ans = s = 0
        for x in nums:
            s += x % modulo == k
            ans += cnt[(s - k) % modulo]
            cnt[s % modulo] += 1
        return ans
