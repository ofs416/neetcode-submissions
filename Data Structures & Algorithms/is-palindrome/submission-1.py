class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.replace(" ", "")
        s = s.lower()
        for idx, char in enumerate(s):
            if not char.isalnum():
                s = s.replace(char, "")
                
        if s == s[::-1]:
            return True

        return False