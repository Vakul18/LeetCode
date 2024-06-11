'''
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
'''

class Solution:
    
	def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
		c = 0
		result = None
		curr = None
		a = l1.val
		b = l2.val
		while True:
			print(f"a : {a} : b : {b} : c : {c}")
			sum = a + b + c
			value = sum % 10
			print(f"value : {value}")
			c = int(sum/10)
			node = ListNode(value)
			if result is None:
				result = node
				curr = node
			else :
				curr.next = node
				curr = node
			
			if l1.next is None and l2.next is None and (c == 0):
				break
			
			if l1.next is not None:
				l1 = l1.next
				a = l1.val
			else:
				a = 0
				
			if l2.next is not None:
				l2 = l2.next
				b = l2.val
			else:
				b = 0
				
		x = result
		while(x is not None):
			print(f"x : {x.val}")
			x = x.next
				
		return result
        
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        p1, p2 = l1, l2
        head = ListNode()
        tmp_p = head
        remain = 0
        while p1 or p2 or remain!=0:
            tmp_sum = remain
            if p1: 
                tmp_sum+=p1.val
                p1 = p1.next
            if p2: 
                tmp_sum+=p2.val
                p2 = p2.next
            tmp_p.next = ListNode(tmp_sum%10)
            tmp_p = tmp_p.next
            remain = tmp_sum//10
        return head.next