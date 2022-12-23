class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        return sum(1 if operation[1] == '+' else -1 for operation in operations)
