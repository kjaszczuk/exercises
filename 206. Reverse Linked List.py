# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        previous = None
        while current:
            next_node = current.next # make copy of next
            current.next = previous # reassign it to previous (for head it's None)
            previous = current # save current to previous
            current = next_node # move to next
        return previous
      # 100, 79
