"""
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

[-9,3] [5,7]

-9 - 3
      |
5 - 7
|
dummy - -9 - 3
             |
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
	def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
		head1 = list1
		head2 = list2

		head = ListNode()

		if not head1:
			return head2
		elif not head2:
			return head1

		curr_node = head

		while head2 and head1:
			if head2.val <= head1.val:
				curr_node.next = head2
				head2 = head2.next
			else:
				curr_node.next = head1
				head1 = head1.next

			curr_node = curr_node.next	
	

		while head2:
			curr_node.next = head2
			head2 = head2.next
			curr_node = curr_node.next

		while head1:
			curr_node.next = head1
			head1 = head1.next
			curr_node = curr_node.next

		return head.next

























# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
	def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
		head1 = list1
		head2 = list2

		head = ListNode()

		if not head1:
			return head2
		elif not head2:
			return head1

		curr_node = head

		while head2 and head1:
			if head2.val <= head1.val:
				curr_node.next = head2
				head2 = head2.next
			else:
				curr_node.next = head1
				head1 = head1.next

			curr_node = curr_node.next	
		curr_node.next = head1 if head1 else head2

		return head.next