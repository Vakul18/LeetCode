"""
find triple such that a^2 + b^2 = c^2
"""
def pythagorean_triplet_exists(arr : list[int]) -> bool:
  sqr_arr = [x**2  for x in arr]
  sqr_arr = sorted(sqr_arr)
  n = len(arr)
  
  for idx in range(n-1, -1, -1):
    i, j = 0, idx - 1
    target = sqr_arr[idx]
    
    while i < j:
      curr_sum = sqr_arr[i] + sqr_arr[j]
      if curr_sum == target:
        return True

      if curr_sum < target:
        i += 1
      else:
        j -= 1    

    return False