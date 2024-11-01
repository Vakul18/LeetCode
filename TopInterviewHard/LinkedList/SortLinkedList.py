"""
Sort linked list

4-2-1-3
quicksort(4,3)
	2-4-1-3
	2-1-4-3
	2-1-3-4
	return 2, 3, None, 4
	
2-1-3-4

quicksort(2,3)
	1-2-3-4
	return 1,1,3,3	

[-1,5,3,4,0]

	return -1, None, 5, 0

[3,2,1]
	2-1-3
	return 2,1,3,3
	2-1-[3]
	return 1,1,2,2
	

"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
	
	def partition(self, head, tail):
		pivot = head
		pivotPrev = None
		curr = head.next
		prev = head
		end = tail.next
		while curr != end:
			if pivot.val > curr.val:
				if not pivotPrev:
					head = curr
				else:
					pivotPrev.next = curr			
				pivotPrev = curr
				tempNode = curr.next
				curr.next = pivot
				prev.next = tempNode
				if prev.next == end:
					tail = prev
				curr = prev
			prev = curr
			curr = curr.next

		return head,pivotPrev, pivot, tail
				
	
	def quicksort(self, head, tail):
		if head == tail or not head or not tail:
			return head, tail
		headPart,pivotPrev, pivot, tailPart = self.partition(head,tail)
		head1,tail1 = self.quicksort(headPart, pivotPrev)
		if pivot.next == tailPart.next:
			head2, tail2 = pivot.next, tailPart 
		else:
			head2, tail2 = self.quicksort(pivot.next, tailPart) 
		pivot.next = head2
		return head1, tail2
	
	def getTail(self, head):
		curr = head
		prev = None
		while curr:
			prev = curr
			curr = curr.next
		return prev
	
	def isSorted(self, head):
		curr = head
		prev = None
		while curr:
			if prev and curr.val < prev.val:
				return False
			prev = curr
			curr = curr.next
		return True

	
		
	def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
		if(self.isSorted(head)):
			return head
		tail = self.getTail(head)
		headSort, tailSort = self.quicksort(head, tail)
		return headSort



4-2-1-3

4-2-1-3

3-2-1-4




# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
	
	def partition(self, head, tail):
		pivot = head
		pre = head
		curr = head


		while curr != tail.next:
			if curr.val < pivot.val:
				curr.val, pre.next.val = pre.next.val, curr.val
				pre = pre.next
        
			curr = curr.next

		pivot.val, pre.val = pre.val, pivot.val
		return pre

	
	def quicksort(self, head, tail):
		if head == tail or not head or not tail:
			return head, tail
		pivot = self.partition(head,tail)
		self.quicksort(head, pivot)
		self.quicksort(pivot.next, tail) 
	
	def getTail(self, head):
		curr = head
		prev = None
		while curr:
			prev = curr
			curr = curr.next
		return prev
	


	
		
	def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:

		tail = self.getTail(head)
		self.quicksort(head, tail)
		return head


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
	
	def split(self, head):
		fast = head
		slow = head


		while fast and fast.next:
			fast = fast.next.next
			if fast:
				slow = slow.next


		second = slow.next
		slow.next = None
		return second

	def merge(self, first, second):
		if not first:
			return second
		if not second:
			return first

		if first.val < second.val:
			first.next = self.merge(first.next, second)
			return first
		else:
			second.next = self.merge(first, second.next)
			return second

	def merge_sort(self, head):
		if not head or not head.next:
			return head
		second = self.split(head)
		head = self.merge_sort(head)
		second = self.merge_sort(second)

		return self.merge(head, second)


		
	def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:

		head = self.merge_sort(head)
		return head