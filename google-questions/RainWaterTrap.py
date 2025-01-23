"""
Given an array arr[] with non-negative integers representing the height of blocks. If the width of each block is 1, compute how much water can be trapped between the blocks during the rainy season

arr[] = [3, 0, 0, 2, 0, 4] -> 10

|    |
|    |   
|  | |   
|__|_|_|_|_


max_height = 4
height_idx = 0 - 3
emptySlots = 0
waterQty = 0
arr[idx] < height_idx+1
	empty_slots +=1
else
	waterQty += empty_slots
	empty_slots = 0
"""

class Solution:
    def trappingWater(self, arr):
        if len(arr) == 0:
            return 0

        max_height = arr[0]
        for element in arr:
            max_height = max(max_height, element)

        water_qty = 0
        """
        max_height = 4
        arr = [1, 0, 0, 2, 0, 4, 0]
        water_qty = 3
        """
        for height in range(1, max_height+1):
        """
        height = 1
        """
            empty_slots = 0
            boundary_found = False
            """
            empty_slots = 1
            boundary_found = True
            block = 0
            """
            for block in arr:
                if block >= height:
                    if boundary_found:
                        water_qty += empty_slots
                        empty_slots = 0
                    else:
                        boundary_found = True
                elif block < height and boundary_found:
                    empty_slots += 1

        return water_qty

class Solution:
    def trappingWater(self, arr):
        left_max = 0
        right_max = 0
        left = 0
        right = len(arr) - 1
        water_qty = 0
        while left <= right:
            if arr[left] < arr[right]:
                if arr[left] > left_max:
                    left_max = arr[left]
                else:
                    water_qty += left_max - arr[left]
                left += 1
            else:
                if arr[right] > right_max:
                    right_max = arr[right]
                else:
                    water_qty += right_max - arr[right]
                right -= 1

        return water_qty