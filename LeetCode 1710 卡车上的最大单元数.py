class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x: -x[1])
        ans = 0
        for box in boxTypes:
            if truckSize >= box[0]:
                ans += box[0] * box[1]
                truckSize -= box[0]
            else:
                ans += truckSize * box[1]
                break
        return ans
