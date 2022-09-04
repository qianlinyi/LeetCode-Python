from queue import PriorityQueue
from typing import List


class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        q, free = PriorityQueue(), PriorityQueue()
        cnt, mx, ans = [0 for _ in range(n)], 0, 0
        for i in range(n):
            free.put(i)
        for meeting in sorted(meetings, key=lambda p: p[0]):
            # 计算空闲会议室
            while q.qsize():
                endTime, index = q.queue[0]
                if meeting[0] >= endTime:
                    free.put(index)
                    q.get()
                else:
                    break
            if free.qsize() == 0:
                endTime, index = q.get()
                cnt[index] += 1
                if cnt[index] > mx:
                    mx = cnt[index]
                    ans = index
                elif cnt[index] == mx:
                    ans = min(ans, index)
                q.put((endTime + meeting[1] - meeting[0], index))
            else:
                index = free.get()
                cnt[index] += 1
                if cnt[index] > mx:
                    mx = cnt[index]
                    ans = index
                elif cnt[index] == mx:
                    ans = min(ans, index)
                q.put((meeting[1], index))
        for index, num in enumerate(cnt):
            if num == mx:
                return index
