class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.replace(" ", "")
        s = s.lower()
        for idx, char in enumerate(s):
            if 97 <= ord(char) <= 125 or 48 <= ord(char) <= 57:
                pass
            else:
                s = s.replace(char, "")

        if s == s[::-1]:
            return True

        return False