class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head.next

        while curr:
            if curr.next.val != 0:
                curr.val += curr.next.val
                curr.next = curr.next.next
            else:
                curr.next = curr.next.next
                curr = curr.next

        return head.next