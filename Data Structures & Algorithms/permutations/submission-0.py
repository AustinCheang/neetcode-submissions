class Solution:
    # Time: O(n * n!) | Space: O(n)
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        path = []
        used = [False] * len(nums)

        self.backtracking(nums, used, path, result)
        return result

    def backtracking(self, nums, used, path, result):
        if len(path) == len(nums):
            result.append(path.copy())
            return

        for i in range(len(nums)):
            if used[i]:
                continue

            used[i] = True
            path.append(nums[i])

            self.backtracking(nums, used, path, result)

            path.pop()
            used[i] = False

            
