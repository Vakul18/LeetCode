"""
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:

MinStack() initializes the stack object.
void push(int val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.
You must implement a solution with O(1) time complexity for each function.

Input
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

Output
[null,null,null,null,-3,null,0,-2]


[-2, 0, -3]

"""
class MinStack:

	def __init__(self):
		self.elements = []

	def push(self, val: int) -> None:
		prev_min = float('inf')
		if len(self.elements) > 0 :        
			prev_min = self.elements[-1][1]
		self.elements.append((val, min(prev_min, val)))
		
	def pop(self) -> None:
		self.elements.pop()
        

	def top(self) -> int:
		if len(self.elements) > 0 :
			return self.elements[-1][0]
		return None
        

	def getMin(self) -> int:
		if len(self.elements) > 0 :
			return self.elements[-1][1]
		return None	
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()