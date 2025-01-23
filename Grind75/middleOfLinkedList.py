"""
Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.

[1,2,3,4,5]

"""
import math

class Solution:
	def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
		no_of_elements = 0
		
		ptr = head
		while ptr:
			no_of_elements += 1
			ptr = ptr.next

		mid = no_of_elements//2 + 1
		
		ptr = head
		while mid > 1:
			ptr = ptr.next
			mid -= 1
		return ptr