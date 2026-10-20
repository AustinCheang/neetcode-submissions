class Solution:
    # Time: O(n) | Space: O(n)
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ["+", "-", "*", "/"]

        for token in tokens:
            if token not in operators:
                stack.append(int(token))

            else:
                second = stack.pop()
                first = stack.pop()

                if token == "+":
                    val = first + second
                elif token == "-":
                    val = first - second
                elif token == "*":
                    val = first * second
                elif token == "/":
                    val = int(first / second)
                stack.append(val)

        return stack[0]