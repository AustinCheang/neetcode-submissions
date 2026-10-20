class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        self.backtrack("", 0, 0, n, result)
        return result

    def backtrack(self, current_str: str, left: int, right: int, n: int, result: List[str]) -> None:

        if len(current_str) == 2 * n:
            result.append(current_str)
            return

        if left < n:
            self.backtrack(current_str + "(", left + 1, right, n, result)

        if right < left:
            self.backtrack(current_str + ")", left, right + 1, n, result)