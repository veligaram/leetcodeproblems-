# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        curr=list1
        t=0
        var=None
        while curr!=None:
            t+=1
            if t==b+1:
                break
            if a==t:
                pp=curr.next
                var=curr
                var.next=list2
                # curr.next=None
                curr=pp
            curr=curr.next
        temp=list1
        while temp!=None:
            if temp.next==None:
                break
            temp=temp.next
        temp.next=curr
        return list1

        
                