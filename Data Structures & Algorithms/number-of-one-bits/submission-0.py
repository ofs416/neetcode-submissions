class Solution:
    def hammingWeight(self, n: int) -> int:
        comp = 2**0
        result = 0
        for i in range(32):
            result += 1 if comp &  n else 0
            comp *= 2

        return result