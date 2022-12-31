class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        n = len(seats)
        seats.sort()
        students.sort()
        return sum(abs(seats[i] - students[i]) for i in range(n))
