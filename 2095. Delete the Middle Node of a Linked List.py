# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nodes_count = 0
        itr = head
        while itr:
            itr = itr.next
            nodes_count += 1
        if nodes_count == 1:
            return None
        itr = head
        for i in range (nodes_count//2-1):
            itr = itr.next
        itr.next = itr.next.next
        return head
# 29, 24
