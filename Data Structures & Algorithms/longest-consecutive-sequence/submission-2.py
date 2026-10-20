class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)

        max_len = 0
        for num in nums:
            if num - 1 not in seen:
                curr = num

                while curr in seen:
                    curr += 1

                max_len = max(max_len, curr - num)

        return max_len

