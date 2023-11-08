class Solution:

    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        spare = ans = 0
        minSpare = 10**18
        for i in range(n):
            spare += gas[i] - cost[i]
            if spare <= minSpare:
                minSpare = spare
                ans = i
        return -1 if spare < 0 else (ans + 1) % n
