from collections import Counter

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0, 0

        c = Counter(s[l])
        current_length = 1
        req_changes = 0

        max_length = 1

        while r < len(s):
            
            if req_changes > k:
                c[s[l]] = c[s[l]] - 1
                l += 1
            elif r + 1 == len(s):
                max_length = max(max_length, current_length)
                break
            else:
                max_length = max(max_length, current_length)
                r += 1
                c[s[r]] = c[s[r]] + 1


            current_length = sum(c.values())
            req_changes = current_length - c.most_common(1)[0][1]
            
            print(s[l:r+1], req_changes)

            

        return max_length