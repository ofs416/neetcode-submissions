class Solution:
    def trap(self, height: List[int]) -> int:
        length = len(height)
        leftMax, rightMax = [0]*length, [0]*length

        for i,j  in zip(range(length), reversed(range(length))):
            leftMax[i] = max(*leftMax[:i+1], height[i])
            rightMax[j] = max(*rightMax[j:], height[j])

        vol = 0
        l, r = 0, 2
        for i in range(length):
            vol += min(leftMax[i], rightMax[i]) - height[i]
            l += 1
            r += 1

        return vol
            