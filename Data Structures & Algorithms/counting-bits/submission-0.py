class Solution:
    def countBits(self, n: int) -> List[int]:
        result = []

        for nums in range(n+1):
            result.append(bin(nums).count('1'))

        return result