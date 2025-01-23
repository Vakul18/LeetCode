"""
Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.


"""

class Solution:
	def hasCycle(self, head: Optional[ListNode]) -> bool:
		if head is None:
			return False
        	
		ptr_2x = head.next if head else None
		ptr = head
		
		while ptr != ptr_2x:
			if not (ptr and ptr_2x):
				return False
			ptr = ptr.next
			ptr_2x = ptr_2x.next.next if ptr_2x.next else None  
		
		return True		
