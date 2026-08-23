from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count_s, count_t = Counter(s), Counter(t)
        if count_s == count_t:
            return True
        return False