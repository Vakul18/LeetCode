"""
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:

MinStack() initializes the stack object.
void push(int val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.
You must implement a solution with O(1) time complexity for each function.

1 0 -2 -3 4 -5 -5

st: [1,0]
min_st : [1,0]
"""
class MinStack:

  def __init__(self):
    self.st = []
    self.min_st = []

  def push(self, val: int) -> None:
    self.st.append(val)
    if not self.min_st or self.min_st[-1] >= val:
      self.min_st.append(val)

  def pop(self) -> None:
    if not self.st:
      return
    top_val = self.st[-1]
    self.st.pop()

    if top_val == self.min_st[-1]:
      self.min_st.pop()       

  def top(self) -> int:
    return self.st[-1] if self.st else None
        

  def getMin(self) -> int:
    return self.min_st[-1] if self.min_st else None
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()