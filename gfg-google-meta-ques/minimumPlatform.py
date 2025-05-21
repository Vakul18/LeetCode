"""

"""

class Solution:    
  def minimumPlatform(self,arr,dep):
    n = len(arr)
    arr_s = sorted(arr)
    dep_s = sorted(dep)
    a, d = 0, 0
    max_platform = 0
    no_of_platform = 0
    while a < n:
      while d < n and dep_s[d] < arr_s[a]:
        no_of_platform -=1
        d += 1
      if d == n:
        break
      no_of_platform += 1
      max_platform = max(no_of_platform, max_platform)
      a += 1

    return max_platform


##################################################################

class Solution:    
  def minimumPlatform(self,arr,dep):
    n = len(arr)
    arr_s = sorted(arr)
    dep_s = sorted(dep)
    a, d = 0, 0
    max_platform = 0
    no_of_platform = 0
    while a < n and d < n:
      if dep_s[d] < arr_s[a]:
        no_of_platform -=1
        d += 1
      else:
        no_of_platform += 1
        max_platform = max(no_of_platform, max_platform)
        a += 1

    return max_platform