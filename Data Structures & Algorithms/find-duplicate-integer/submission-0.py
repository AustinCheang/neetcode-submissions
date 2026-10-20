class Solution:
    # Time: O(n) | Space: O(1)
    def findDuplicate(self, nums: List[int]) -> int:
        slow = 0
        fast = 0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break

        # reset slow to beginning
        slow = 0

        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow