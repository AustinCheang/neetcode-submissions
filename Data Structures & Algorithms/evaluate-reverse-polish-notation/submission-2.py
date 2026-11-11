# Time: O(n) | Space: O(n)
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for t in tokens:
            if t not in ["+", "-", "*", "/"]:
                stack.append(int(t))
                continue


            second = int(stack.pop())
            first = int(stack.pop())

            if t == "+":
                val = first + second
            elif t == "-":
                val = first - second
            elif t == "*":
                val = first * second
            elif t == "/" and second != 0:
                val = int(first / second)
                
            stack.append(val)

        return stack[0]
                

