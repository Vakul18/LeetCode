"""
Given the head of a singly linked list, reverse the list, and return the reversed list.

1-2-3-4-5 -> 5-4-3-2-1

head : 1, tail : 5
1-2-3-4-5 -> 2-1-3-4-5 -> 3-2-1-4-5 

1-2-3-4-5 -> 

head, tail : 1

iterate over linked list

1. move the elemnt next to tail, before the head and join tail to next of that element
2. iterate till we reach last element in the list



"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
  def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    tail = head
    curr = head
    while tail and tail.next:
      next = tail.next
      next_next = next.next
      next.next = head
      head = next
      tail.next = next_next

    return head
