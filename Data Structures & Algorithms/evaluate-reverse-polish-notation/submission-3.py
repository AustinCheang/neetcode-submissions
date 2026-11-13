# Time: O(n) | Space: O(n)
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for t in tokens:
            if t not in {"+", "-", "*", "/"}:
                stack.append(int(t))
                continue

            num_2 = stack.pop()
            num_1 = stack.pop()

            result = 0
            if t == "+":
                result = num_1 + num_2
            elif t == "-":
                result = num_1 - num_2
            elif t == "*":
                result = num_1 * num_2
            else:
                quotient = abs(num_1) // abs(num_2)
                result = -quotient if (num_1 < 0) != (num_2 < 0) else quotient

            stack.append(result)

        return stack[0]