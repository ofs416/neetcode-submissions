from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            pass
        elif Counter(s) == Counter(t):
            return True

        return False