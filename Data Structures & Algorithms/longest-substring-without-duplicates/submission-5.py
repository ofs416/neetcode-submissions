class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2:
            return len(s)
        
        l, r = 0, 1

        maxLength = 1

        while r < len(s):

            
            length = 1 + r - l
            if s[l] == s[r]:
                r += 1
            elif len(set(s[l:r+1])) != length:
                l += 1
            else:
                r+=1
                maxLength = max(maxLength, length)
            print(s[l:r+1], maxLength)
            
        return maxLength

            
