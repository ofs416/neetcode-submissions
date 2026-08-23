from collections import Counter

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0

        c = Counter()
        max_length = 0

        for r in range(len(s)):
            c[s[r]] = c[s[r]] + 1
            
            while sum(c.values()) - c.most_common(1)[0][1] > k:
                c[s[l]] = c[s[l]] - 1
                l += 1
        
            max_length = max(max_length, sum(c.values()))
            
        return max_length