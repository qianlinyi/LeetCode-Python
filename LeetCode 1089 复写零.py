from typing import List


# 双指针 + 栈
class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        n = len(arr)
        top, i = 0, -1
        while top < n:
            i += 1
            top += 1 if arr[i] else 2
        j = n - 1
        if top == n + 1:
            arr[j] = 0
            j -= 1
            i -= 1
        while j >= 0:
            arr[j] = arr[i]
            j -= 1
            if arr[i] == 0:
                arr[j] = arr[i]
                j -= 1
            i -= 1
