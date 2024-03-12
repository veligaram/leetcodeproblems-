class Solution:
	def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
		dummy = ListNode(0, head)
		prefix, dict_prefix = 0, {0:dummy}
		while head:
			prefix += head.val
			if prefix in dict_prefix:
				dict_prefix[prefix].next = head.next
				head = dict_prefix[prefix]
				while prefix in dict_prefix:
					dict_prefix.popitem()
			dict_prefix[prefix] = head
			head = head.next
		return dummy.next