# Time: O(n) | Space: O(n)
class Solution:
    def isValid(self, s: str) -> bool:
        parenthese_map = {
            ']': '[',
            ')': '(',
            '}': '{'
        }

        stack = []

        for c in s:
            if c in parenthese_map:
                if not stack:
                    return False
                curr_opening = stack.pop()
                
                if parenthese_map[c] != curr_opening:
                    return False
            elif c in parenthese_map.values():
                stack.append(c)

        return len(stack) == 0
            