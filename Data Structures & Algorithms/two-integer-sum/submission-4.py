class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complement_map = dict()

        for i, num in enumerate(nums):
            complement = target - num

            if complement in complement_map:
                return [complement_map[complement], i]

            complement_map[num] = i

        return []