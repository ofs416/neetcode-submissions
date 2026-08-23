from collections import Counter

class Solution:
    def hammingWeight(self, n: int) -> int:
        n = Counter(bin(n))
        
        try:
            return n["1"]
        except:
            return 0
