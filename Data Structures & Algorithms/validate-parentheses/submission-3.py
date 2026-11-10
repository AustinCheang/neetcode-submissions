# Time: O(n) | Space: O(n)
class Solution:
    def isValid(self, s: str) -> bool:
        parenthese_dict = {
            "]": "[", "}": "{", ")": "("
        }

        stack = []

        for xs in s:
            if stack and xs in parenthese_dict:
                last = stack.pop()

                if last != parenthese_dict[xs]:
                    return False
            else:
                stack.append(xs)

        return len(stack) == 0