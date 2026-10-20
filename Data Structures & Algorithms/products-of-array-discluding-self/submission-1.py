class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [1] * n

        # step 1: calculate left products in-place
        for i in range(1, n):
            result[i] = result[i - 1] * nums[i - 1]

        # step 2: calculate right products in-place
        right_product = 1
        for i in range(n - 1, -1, -1):
            result[i] *= right_product
            right_product *= nums[i]

        return result

        