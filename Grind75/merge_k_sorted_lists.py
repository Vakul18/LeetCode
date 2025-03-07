"""
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

1-2-3
4-5-16
1-5-6

[head1,head2...headk]

1-1-2-3-4-5-5-16

"""
import heapq

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
	def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
		priority_queue = []
		head = ListNode()
		for idx, node in enumerate(lists):
			if node:
				heapq.heappush(priority_queue, (node.val, idx, node))
		curr_node = head
		while len(priority_queue)>0:
			value, idx, min_node = heapq.heappop(priority_queue)
			curr_node.next = min_node
			curr_node = curr_node.next
			min_node = min_node.next
			if min_node:
				heapq.heappush(priority_queue, (min_node.val, idx, min_node))

		return head.next		