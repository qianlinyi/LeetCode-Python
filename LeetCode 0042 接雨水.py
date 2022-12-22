class Solution:
    def trap(self, height: List[int]) -> int:
        ans = 0
        st = []
        for i, h in enumerate(height):
            while st and h > height[st[-1]]:
                mid = st.pop()
                if not st:
                    break
                left = st[-1]
                ans += (min(height[left], h) - height[mid]) * (i - left - 1)
            st.append(i)
        return ans
