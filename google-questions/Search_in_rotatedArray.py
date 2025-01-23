"""
Given a sorted and rotated array arr[] of distinct elements, the task is to find the index of a target key. Return -1 if the key is not found.

arr[] = [5, 6, 7, 8, 9, 10, 1, 2, 3], key = 14

arr[] = [7, 8, 9, 10, 1, 2, 3, 5, 6], key = 3

arr[] = [2,3,4,1]


left = 0, right = n
mid = (left+right)//2
mid = 4

if arr[mid] > key and arr[mid-1] < arr[mid]:
 


"""
class Solution:
    def search(self,arr,key):
        n = len(arr)
        left = 0
        right = n-1
        while(left <= right):
            mid = (left+right)//2
            if arr[mid] == key:
                return mid
            
            # find sorted half
            if arr[left] <= arr[mid]:
                if key >= arr[left] and key <= arr[mid]:
                    right = mid-1
                else:
                    left = mid+1
            else:
                if arr[right] >= arr[mid]:
                    if key >= arr[mid] and key <= arr[right]:
                        left = mid + 1
                    else:
                        right = mid - 1

        return -1





def search(arr, n, k):
    low = 0
    high = n - 1
    while low <= high:
        mid = (low + high) // 2

        # if mid points the target
        if arr[mid] == k:
            return mid

        # if left part is sorted
        if arr[low] <= arr[mid]:
            if arr[low] <= k and k <= arr[mid]:
                # element exists
                high = mid - 1
            else:
                # element does not exist
                low = mid + 1
        else:  # if right part is sorted
            if arr[mid] <= k and k <= arr[high]:
                # element exists
                low = mid + 1
            else:
                # element does not exist
                high = mid - 1
    return -1	        
         
            