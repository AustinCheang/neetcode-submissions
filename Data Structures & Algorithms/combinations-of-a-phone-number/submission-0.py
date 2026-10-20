class Solution:
    # Time: O(n * 4^n) | Space: O(n)
    def letterCombinations(self, digits: str) -> List[str]:
        result = []
        digit_to_char = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz"
        }

        if digits:
            self.backtracking(digits, digit_to_char, 0, "", result)
        return result

        
    def backtracking(self, digits, digit_to_char, start_idx, path, result):
        if len(path) == len(digits):
            result.append(path)
            return

        for c in digit_to_char[digits[start_idx]]:
            self.backtracking(digits, digit_to_char, start_idx + 1, path + c, result)

    