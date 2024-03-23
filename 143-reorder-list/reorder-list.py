# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        res = ListNode(0)
        res.next = head
        slow = fast = res
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next 
        fast = slow.next
        slow.next = None
        fast = self.reverseTwo(fast)
        slow = res.next
        while fast:
            slowp, fastp = slow.next, fast.next
            slow.next, fast.next = fast, slowp
            slow, fast = slowp, fastp
        return res.next


    def reverseTwo(self, node):
        prev = None
        curr = node
        while curr:
            nextp = curr.next
            curr.next = prev
            prev = curr
            curr = nextp
        return prev