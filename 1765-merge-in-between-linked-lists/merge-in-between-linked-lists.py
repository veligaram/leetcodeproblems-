# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        curr=list2
        while curr.next:
            curr=curr.next
        list2_end=curr
        curr=list1
        n=0
        while 1:
            if n==a-1:
                temp=curr
                while 1:
                    if n==b+1:
                        temp.next=list2
                        list2_end.next=curr
                        return list1
                    curr=curr.next    
                    n+=1
            curr=curr.next
            n+=1

        
        