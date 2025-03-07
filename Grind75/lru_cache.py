"""
Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:

LRUCache(int capacity) Initialize the LRU cache with positive size capacity.

int get(int key) Return the value of the key if the key exists, otherwise return -1.

void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.

The functions get and put must each run in O(1) average time complexity.


1. Create doubly linked list.[maintain pointer to both head and tail]
2. maintain a dict which maps keys to nodes in linked list.
3. While put if the capacity is remove from front and add to the back of linked list.
4. during get remove the element from the linked list and add to end of the queue.

capa = 2
[(1,1), (3,3)]

"""
from collections import deque
from typing import TypeVar, Generic

T = TypeVar("T")

class LRUCache():

	class DoubleLinkedList(Generic[T]):
		def __init__(self):
			self.head = None
			self.tail = None

		class Node:
			def __init__(self, prev, next, value):
				self.prev = prev
				self.next = next
				self.value = value
		
		def append(self, value : T) -> Node:
			node = self.Node(None, None, value)
			if not self.head:
				self.head, self.tail = node, node
				return self.tail

			tail = self.tail
			tail.next = node
			node.prev = tail
			self.tail = node

			#h = self.head
			#l = []
			#while h:
				#l.append(h.value)
				#h = h.next
			#print(l)

			return self.tail

		def remove_left(self) -> None:
			head = self.head
			self.head = self.head.next
			if not head:
				self.tail = None
			return head.value

		def remove(self, node: Node):
			prev_node = node.prev
			next_node = node.next
			if prev_node:
				prev_node.next = next_node
			if next_node:
				next_node.prev = prev_node
			if self.head == node:
				self.head = next_node
			if self.tail == node:
				self.tail = prev_node
				

	def __init__(self, capacity: int):
		self.max_capacity = capacity
		self.list = self.DoubleLinkedList[int]()
		self.key_to_node = dict()
        
	def get(self, key: int) -> int:
		if key in self.key_to_node:
			node = self.key_to_node[key]
			self.list.remove(node)
			node = self.list.append(node.value)
			self.key_to_node[key] = node
			return node.value[1]
		return -1
        
	def put(self, key: int, value: int) -> None:
		node = None
		if key in self.key_to_node:
			node = self.key_to_node[key]
			self.list.remove(node)
			node = self.list.append((key, value))
		else:
			curr_capacity = len(self.key_to_node)
			
			if curr_capacity == self.max_capacity:
				key_value = self.list.remove_left()
				self.key_to_node.pop(key_value[0])
			
			node = self.list.append((key, value))
			
		self.key_to_node[key] = node
				



from collections import OrderedDict
class LRUCache:
 def __init__(self, capacity: int):
  self.cache = OrderedDict()
  self.capacity = capacity
 def get(self, key: int) -> int:
  if key not in self.cache:
   return -1
  self.cache.move_to_end(key)
  return self.cache[key]
 def put(self, key: int, value: int) -> None:
  if key in self.cache:
   self.cache.move_to_end(key)
  self.cache[key] = value
  if len(self.cache) > self.capacity:
   self.cache.popitem(last=False)




# 1. access value by key and run in O(1)
#  - data type = dictionary
# 2. upsert key and value and run in O(1)
# 3. evict the least recently used.
# 4. all feature run in O(1)



class CacheNode:
    def __init__(self, key=None, value=None, previous=None, next=None):
        self.key = key
        self.value = value
        self.previous = previous
        self.next = next

class LRUCache:

    def __init__(self, capacity: int):
        self.cache_dict = dict()
        self.cache_limit = capacity
        self.cache_size = 0
        self.cache_list_head = CacheNode(0, 0)
        self.cache_list_tail = CacheNode(0, 0)
        self.cache_list_head.next = self.cache_list_tail
        self.cache_list_tail.previous = self.cache_list_head
        

    def get(self, key: int) -> int:
        if key in self.cache_dict:
            result = self.cache_dict[key].value
            self.__refresh(self.cache_dict[key])
            return result
        else:
            return -1

        
            
    def put(self, key: int, value: int) -> None:
        if key in self.cache_dict:
            self.cache_dict[key].value = value
        else:
            self.cache_dict[key] = CacheNode(key, value)

            self.cache_size += 1
            if self.cache_size > self.cache_limit:
                self.__evict()

        self.__refresh(self.cache_dict[key])
        

    def __evict(self) -> None:
        temp = self.cache_list_head.next
        self.cache_list_head.next = temp.next
        temp.next.previous = self.cache_list_head 
        del self.cache_dict[temp.key]

    def __refresh(self, node):
        if node.next and node.previous:
            node.next.previous = node.previous
            node.previous.next = node.next
        self.cache_list_tail.previous.next = node
        node.next = self.cache_list_tail
        node.previous = self.cache_list_tail.previous
        self.cache_list_tail.previous = node



        
        
            


        


        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
        