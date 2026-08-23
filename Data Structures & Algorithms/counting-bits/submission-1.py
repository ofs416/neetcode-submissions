class Solution:
    def countBits(self, n: int) -> List[int]:
        result = [0] * (n + 1)

        for nums in range(n+1):
            result[nums] = bin(nums).count('1')

        return result