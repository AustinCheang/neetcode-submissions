class Solution:
    # Time: O(2^n) | Space: O(n)
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []
        path = []
        self.backtracking(candidates, target, 0, 0, path, result)
        return result

    def backtracking(self, candidates, target, start_idx, curr_sum, path, result):
        if curr_sum == target:
            result.append(path[:])
            return

        if curr_sum > target:
            return

        for i in range(start_idx, len(candidates)):
            if i > start_idx and candidates[i] == candidates[i - 1]:
                continue
            new_val = candidates[i]

            if curr_sum + new_val > target:
                break

            path.append(new_val)

            self.backtracking(candidates, target, i + 1, curr_sum + new_val, path, result)

            path.pop()

