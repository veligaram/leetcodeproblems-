# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        x1=head
        x2=head
        while x2 is not None and x2.next is not None:
            x1=x1.next
            x2=x2.next.next
        return x1    