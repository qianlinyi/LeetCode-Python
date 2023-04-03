class Solution:
    def makeSubKSumEqual(self, arr: List[int], k: int) -> int:
        k = gcd(k, len(arr))
        ans = 0
        for i in range(k):
            b = sorted(arr[i::k])
            mid = b[len(b) // 2]
            ans += sum(abs(x - mid) for x in b)
        return ans
