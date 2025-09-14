# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        itr = head
        count = 0
        max_twin = 0
        while itr:
            itr = itr.next
            count += 1
        itr = head
        prev = None
        for i in range (count//2):
            next_node = itr.next
            itr.next = prev
            if (i == count//2 - 1):
                break
            prev = itr
            itr = next_node
        while itr:
            twin_sum = itr.val + next_node.val
            if max_twin < twin_sum:
                max_twin = twin_sum
            itr = itr.next
            next_node = next_node.next
        return max_twin
# 21, 90
