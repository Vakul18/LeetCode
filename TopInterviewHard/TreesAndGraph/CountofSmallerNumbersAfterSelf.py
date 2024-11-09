"""
Given an integer array nums, return an integer array counts where counts[i] is the number of smaller elements to the right of nums[i].
"""
"""

This approach will not work as we need to check the right sub tree also, in case the node is not the largest.
0 1  2  3 10 11
2 3 10 11  1  0

       

2 2 2 2 1 0

2 3 10 11  1  0

counts = [0, 1, 2, 2]
heap = [(11,2), (10,2), (0,0), (1,1)]

   11
 10   9
1


heapify(0)
idx = -1
tracker = 0

heeapify(1)
n = 2
idx = 0
tracker = 1
left = 1
right = 2
larg = 1

swap 0 and 1 idx
tracker = 0

idx = 0
left = 1
right = 2

return 1

heapify(11)
n=3
idx=0
tracker=2
left = 1
right = 2
larg = 0
larg=2
tracker=0
return 2

heapify(10)
n = 4
idx = 1
tracker = 3

left = 3
right = 4
larg = 1
larg= 3
swap 3 and 1
tracker = 1
return 2


"""

class Solution:
	
	def heapifyCount(self, heap : List[int], num : int) -> Tuple[int, List]:
		heap.append((num,0))
		n = len(heap)
		idx = int((n - 2)/2)
		tracker = n - 1 
		while idx >= 0 and idx < n:
			leftChild = 2*idx + 1
			rightChild = 2*idx + 2
			largestChild = idx

			if leftChild < n and heap[leftChild][0] > heap[largestChild][0]:
				largestChild = leftChild

			if rightChild < n and heap[rightChild][0] > heap[largestChild][0]:
				largestChild = rightChild

			if largestChild != idx:
				heap[largestChild][1] += (heap[idx][1] + 1)
				heap[idx], heap[largestChild] = heap[largestChild], heap[idx]
				if tracker == idx:
					tracker = largestChild
				elif tracker == largestChild:
					tracker == idx
	
				idx = int((idx - 1)/2)
 			
			else:
				break
		return heap[tracker][1], heap
				
		
		
	
	def countSmaller(self, nums: List[int]) -> List[int]:
		counts = []
		heap = []
		
		for idx in range(len(nums)-1 , -1, -1):
			count, heap = self.heapifyCount(heap, nums[idx])
			counts.append(count)

		counts.reverse()
		return counts




#################################################################################################

"""
[5,2,6,1]

n = 4

mergesort(0,3)

mid = 1

mergesort(0,1)

mergesrot(0,0)
mergesort(1,1)

merge(0,0,1)




"""

class Solution:
	def countSmaller(self, nums: List[int]) -> List[int]:
		n = len(nums)
		counts = [0]*n
		numsIdx = [(num, idx) for idx,num in enumerate(nums)]
		#print(numsIdx)
		self.mergesort(numsIdx, 0, n-1, counts)
		return counts
	
	def mergesort(self, numsIdx, l, r, counts):
		
		if l >= r:
			return

		mid = int((l+r)/2)
		
		self.mergesort(numsIdx, l, mid, counts)
		self.mergesort(numsIdx, mid+1, r, counts)

		self.merge(numsIdx, l, mid, r, counts)
		
		return

	def merge(self, numsIdx, l, m, r, counts):
		#print(f"l:{l}, m:{m}, r:{r}")
		temp_list = []
		lIdx = l
		rIdx = m+1

		while(lIdx<=m and rIdx<=r):
			if numsIdx[lIdx][0] > numsIdx[rIdx][0]:
				counts[numsIdx[lIdx][1]] += r-rIdx+1
				#print(counts)
				temp_list.append(numsIdx[lIdx])
				lIdx += 1
			else:
				temp_list.append(numsIdx[rIdx])
				rIdx += 1

		while lIdx<=m:
			temp_list.append(numsIdx[lIdx])
			lIdx += 1

		while rIdx<=r:
			temp_list.append(numsIdx[rIdx])
			rIdx += 1

		idx = l
		tIdx = 0
		
		while idx <= r:
		
			numsIdx[idx] = temp_list[tIdx]
			idx += 1
			tIdx += 1

		


			
		
	
			
						
	
		




		        	