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
                if stack and match[char] == stack[-1]:
                    stack.pop()
                else:
                    return False

        
        return not stack 
