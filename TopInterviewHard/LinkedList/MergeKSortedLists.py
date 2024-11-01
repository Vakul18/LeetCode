"""
Merge k Sorted Lists	
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

can lists have duplicate elements?
yes

should duplicate elements be in order?

[[3,4,8], [9,0,1]]
[0,1,3,4,8,9]

1 2 3 4 5 6 7 8 9 10 5

1-2 3-4 5-6 7-8 9-10

1-2-3-4 5-6-7-8 9-10 4

1-2-3-4-5-6-7-8 9-10 8



"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

	def mergeLists(self, list1, list2):
		mergedListHead = ListNode(-1, None)
		mergedList = mergedListHead
		while (list1) and (list2) :
			if list1.val <= list2.val :
				mergedList.next = list1
				list1 = list1.next
			else:
				mergedList.next = list2
				list2 = list2.next
			mergedList = mergedList.next

		remainingPt = list1 if (list1) else list2 if (list2)  else None
		

		while (remainingPt) :
			mergedList.next = remainingPt
			mergedList = mergedList.next
			remainingPt = remainingPt.next

		
		return mergedListHead.next
			
			
	
	def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

		if len(lists) == 0:
			return None
		if len(lists) == 1:
			return lists[0]
		
		mergedList = self.mergeLists(lists[0], lists[1])
		idx = 2
		
		while idx < len(lists):
			mergedList = self.mergeLists(mergedList, lists[idx])
			idx += 1
		return mergedList

        			






class Solution:

	def mergeLists(self, list1, list2):
		mergedListHead = ListNode(-1, None)
		mergedList = mergedListHead
		while (list1) and (list2) :
			if list1.val <= list2.val :
				mergedList.next = list1
				list1 = list1.next
			else:
				mergedList.next = list2
				list2 = list2.next
			mergedList = mergedList.next

		remainingPt = list1 if (list1) else list2 if (list2)  else None
		

		while (remainingPt) :
			mergedList.next = remainingPt
			mergedList = mergedList.next
			remainingPt = remainingPt.next

		
		return mergedListHead.next
			
	def mergeSort(self, lists, left, right):
		if left == right :
			return lists[left]
		mid = (left + right)//2
		left = self.mergeSort(lists, left, mid)
		right = self.mergeSort(lists, mid + 1, right)
		
		return self.mergeLists(left, right)
		
	
		
		
		
	
	def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

		if len(lists) == 0:
			return None
		if len(lists) == 1:
			return lists[0]
		
		return self.mergeSort(lists, 0, len(lists) - 1)
		
		return mergedList
	        