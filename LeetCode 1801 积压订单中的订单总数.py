import heapq


class Solution:
    def getNumberOfBacklogOrders(self, orders: List[List[int]]) -> int:
        sell, buy, mod = [], [], 10 ** 9 + 7
        for order in orders:
            price, amount, type = order
            if type == 0:
                while sell and sell[0][0] <= price and amount:
                    p, a = heapq.heappop(sell)
                    if a <= amount:
                        amount -= a
                    else:
                        heapq.heappush(sell, (p, (a - amount) % mod))
                        amount = 0
                if amount:
                    heapq.heappush(buy, (-price, amount % mod))
            else:
                while buy and -buy[0][0] >= price and amount:
                    p, a = heapq.heappop(buy)
                    if a <= amount:
                        amount -= a
                    else:
                        heapq.heappush(buy, (p, (a - amount) % mod))
                        amount = 0
                if amount:
                    heapq.heappush(sell, (price, amount % mod))
        return (sum(_[1] for _ in buy) + sum(_[1] for _ in sell)) % mod
