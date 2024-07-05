# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        if not head or not head.next or not head.next.next:
            return [-1, -1]
        
        minDistance = float('inf')
        firstCrit = None
        lastCrit = None
        counter = 0

        prev = head
        curr = head.next

        while curr.next:
            if prev.val < curr.val and curr.val > curr.next.val:
                if firstCrit == None:
                    firstCrit = counter
                    lastCrit = counter
                else:
                    minDistance = min(minDistance, counter - lastCrit)
                    lastCrit = counter
            elif prev.val > curr.val and curr.val < curr.next.val:
                if firstCrit == None:
                    firstCrit = counter
                    lastCrit = counter
                else:
                    minDistance = min(minDistance, counter - lastCrit)
                    lastCrit = counter

            prev = prev.next
            curr = curr.next
            counter += 1

        if minDistance == float('inf'):
            return [-1, -1]
        else:
            return [minDistance, lastCrit - firstCrit]

                    


        