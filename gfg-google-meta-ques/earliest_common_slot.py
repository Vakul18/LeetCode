"""
You are given two lists of availability time slots, slots1 and slots2, for two people. Each slot is represented as [start, end], and it is gurranted that within each list, no two slots overlap (i.e., for any two intervals, either start1>end2 or start2>end1). Given a metting duration d, return the earliest common time slot of length of least d. If no such slot exits, return an empty array.

Input: slots1 = [[10,50], [60,120], [140,210]], slots2 = [[0,15], [60,70]], d = 8
Output: [60,68]

slots1 = [[10,50], [60,120], [140,210]], slots2 = [[0,15], [60,70]]
            |                                        |

1. sort the slots
2. i,j ptrs
3. checks:
  3.1 check if both the slots can accomodate d, if not incr the corr ptrs.
  3.2 max start, min end, check if accomdates d, if not then incr the ptr with min end
"""
#User function Template for python3
class solution:
  def commonSlot(a, b, d):
    a_s = sorted(a, key= lambda x : x[0])
    b_s = sorted(b, key= lambda x : x[0])

    a_i, b_i = 0, 0
    a_n, b_n = len(a), len(b)
    
    while a_i < a_n and b_i < b_n:
      a_slot, b_slot = a_s[a_i], b_s[b_i]

      if a_slot[1] - a_slot[0] < d:
        a_i += 1
        continue
      
      if b_slot[1] - b_slot[0] < d:
        b_i += 1
        continue
      
      overlap = min(a_slot[1], b_slot[1]) - max(a_slot[0], b_slot[0])

      if overlap >= d:
        return [max(a_slot[0], b_slot[0]), max(a_slot[0], b_slot[0]) + d]
      else:
        if b_slot[1] > a_slot[1]:
          a_i += 1
        else:
          b_i += 1
    return []
    