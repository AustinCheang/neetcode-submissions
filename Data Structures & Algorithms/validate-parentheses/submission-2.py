# Time: O(n) | Space: O(n)
class Solution:
    def isValid(self, s: str) -> bool:
        parenthese_dict = {
            "}": "{",
            "]": "[",
            ")": "("
        }

        stack = []

        for p in s:
            if p not in parenthese_dict:
                stack.append(p)
                continue

            if stack:
                curr = stack.pop()

                if curr != parenthese_dict[p]:
                    return False
            else:
                return False

        return len(stack) == 0