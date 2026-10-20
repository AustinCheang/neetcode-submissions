# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    # Time: O(n) | Space: O(1)
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        while curr:
            # swap nodes
            next_node = curr.next
            curr.next = prev

            # move pointers
            prev = curr
            curr = next_node
        
        return prev
