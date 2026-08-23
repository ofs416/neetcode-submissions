class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        areas = []

        for l in range(0, len(heights)-1):
            for r in range(l+1, len(heights)):
                area = min(heights[l], heights[r]) * (r-l)
                areas.append(area)

        return max(areas)