from bisect import bisect_left

MAXN = 10 ** 6 + 5
prime = []
isPrime = [False, False] + [True] * MAXN
for i in range(2, MAXN):
    if isPrime[i]:
        prime.append(i)
    for p in prime:
        if i * p > MAXN:
            break
        isPrime[i * p] = False
        if i % p == 0:
            break


class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        mn, ans = right, [-1, -1]
        pos = bisect_left(prime, left)
        while prime[pos + 1] <= right:
            gap = prime[pos + 1] - prime[pos]
            if gap < mn:
                mn, ans = gap, [prime[pos], prime[pos + 1]]
            pos += 1
        return ans
