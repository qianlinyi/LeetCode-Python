class Solution:
    def maxNumberOfAlloys(self, n: int, k: int, budget: int, composition: List[List[int]], stock: List[int],
                          cost: List[int]) -> int:
        l, r = 0, 2 * 10 ** 8
        while l <= r:
            mid = l + r >> 1
            flag = 0
            for i in range(k):
                if sum(max(0, (composition[i][j] * mid - stock[j])) * cost[j] for j in range(n)) <= budget:
                    flag = 1
                    break
            if flag:
                l = mid + 1
            else:
                r = mid - 1
        return r
