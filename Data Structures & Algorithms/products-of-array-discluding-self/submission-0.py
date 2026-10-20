class Solution:
    # Time: O(n) | Space: O(n)
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        # Step 1: Calculate product sum from left
        left_products = [1] * n
        for i in range(1, n):
            left_products[i] = left_products[i - 1] * nums[i - 1]

        # Step 2: Calculate product sum from right
        right_products = [1] * n
        for i in range(n-2, -1, -1):
            right_products[i] = right_products[i + 1] * nums[i + 1]

        # Step 3: Combine result
        return [left * right for left, right in zip(left_products, right_products)]