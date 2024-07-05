# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from math import inf
class Solution:        
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        if not head or not head.next:
            return [0, 0]
        
        arr = []
        min_d, max_d = float('inf'), -float('inf')
        first_critical, last_critical = None, None
        while head:
            arr.append(head.val)
            head = head.next
        for i in range(1, len(arr) - 1):
            if (arr[i] > arr[i-1] and arr[i] > arr[i+1]) or (arr[i] < arr[i-1] and arr[i] < arr[i+1]):
                if last_critical is None:
                    first_critical = last_critical = i
                else:
                    min_d = min(min_d, i - last_critical)
                    max_d = max(max_d, i - first_critical)
                    last_critical = i
        if min_d == float('inf') or max_d == -float('inf'):
            return [-1, -1]
        return [min_d, max_d]