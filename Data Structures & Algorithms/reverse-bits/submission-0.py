class Solution:
    def reverseBits(self, n: int) -> int:
        n = bin(n)
        result = 0

        for i, bit in enumerate(n[::-1]):
            if bit == 'b':
                return result

            result += int(bit) * 2**(31-i)

            