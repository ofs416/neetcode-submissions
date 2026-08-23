from collections import Counter

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0, 0

        c = Counter(s[l])

        max_length = 0

        while r < len(s):
            
            if sum(c.values()) - c.most_common(1)[0][1] > k:
                c[s[l]] = c[s[l]] - 1
                l += 1
            elif r + 1 == len(s):
                max_length = max(max_length, sum(c.values()))
                break
            else:
                max_length = max(max_length, sum(c.values()))
                r += 1
                c[s[r]] = c[s[r]] + 1

            
        return max_length