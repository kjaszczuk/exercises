# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow, fast, pre, next_n = head, head, None, head
        max_twin = 0
        while fast:
            fast = fast.next.next if fast.next else None
            next_n = slow.next
            slow.next = pre
            pre = slow
            slow = next_n
        while slow:
            max_twin = max(max_twin, slow.val + pre.val)
            slow, pre = slow.next, pre.next
        return max_twin
# 74, 97
