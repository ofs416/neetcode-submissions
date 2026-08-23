class Solution:
    def isValid(self, s: str) -> bool:
        open_set = set(["{", "[", "("])
        close_set = set(["}", "]", ")"])
        match = {"}":"{", "]":"[", ")":"(",}
        stack = []

        for char in s:
            if char in open_set:
                stack.append(char)
            if char in close_set:
                try:
                    if match[char] != stack.pop():
                        return False
                except:
                    return False
        
        return not stack 
