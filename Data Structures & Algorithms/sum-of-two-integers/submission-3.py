class Solution:



    def getSum(self, a: int, b: int) -> int:

        MAX = 0x7FFFFFFF  # hexa decimal representation of maximum positive 31 bit number
        MASK = 0xFFFFFFFF

        xor = (a ^ b) & MASK
        carry = ((a & b) << 1) & MASK

        if carry == 0:
            return xor if xor <= MAX else ~(xor ^ MASK)
        else:
            return self.getSum(xor, carry)

