class Solution:
    def isValid(self, s: str) -> bool:
        parenthese_map = {')': '(', '}': '{', ']': '['}

        stack = []

        for c in s:
            if c not in parenthese_map:
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False
                    
                last_c = stack.pop()
                if parenthese_map[c] != last_c:
                    return False
        return len(stack) == 0
