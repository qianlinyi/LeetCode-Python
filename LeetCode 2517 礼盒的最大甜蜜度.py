import bisect


class Solution:
    def maximumTastiness(self, price: List[int], k: int) -> int:
        price.sort()

        def check(x):
            cnt = 0
            pre = -1
            for p in price:
                if p > pre:
                    pre = p + x
                    cnt += 1
            return cnt >= k

        l, r = 0, 10 ** 9
        while l <= r:
            # print(l, r)
            mid = l + r >> 1
            if check(mid):
                l = mid + 1
            else:
                r = mid - 1
        return l
