"""
Here's your text, formatted clearly and consistently:

---

You're having a grand old time clicking through the rabbit hole that is your favorite online encyclopedia.

The encyclopedia consists of **N** different web pages, numbered from **1** to **N**. Each page **i** contains nothing but a single link to a different page **L<sub>i</sub>**.

A session spent on this website involves beginning on one of the **N** pages, and then navigating around using the links until you decide to stop. That is, while on page **i**, you may either move to page **L<sub>i</sub>**, or stop your browsing session.

Assuming you can choose which page you begin the session on, what's the **maximum number of different pages** you can visit in a single session?  
**Note:** A page only counts once even if visited multiple times during the session.

---

### Constraints:
- 2 ≤ N ≤ 500,000  
- 1 ≤ L<sub>i</sub> ≤ N  
- L<sub>i</sub> ≠ i  

---

### Sample Test Case #1
- **N = 4**  
- **L = [4, 1, 2, 1]**  
- **Expected Return Value = 4**

### Sample Test Case #2
- **N = 5**  
- **L = [4, 3, 5, 1, 2]**  
- **Expected Return Value = 3**

### Sample Test Case #3
- **N = 5**  
- **L = [2, 4, 2, 2, 3]**  
- **Expected Return Value = 4**

---

### Sample Explanation:

- **Test Case 1:**  
  You can visit all 4 pages in a single browsing session if you begin on page **3**.  
  For example, the sequence: **3 → 2 → 1 → 4**

- **Test Case 2:**  
  You can only visit at most 3 different pages.  
  For example, the sequence: **3 → 5 → 2**

- **Test Case 3:**  
  You can only visit at most 4 different pages.  
  For example, the sequence: **5 → 3 → 2 → 4**


### Sample Test Case #1
- **N = 4**  
- **L = [4, 1, 2, 1]**  
path_count = [i ,i ,i ,i]
max_path  = 0

idx, page = 0,4
path = 1
visited = [0]
curr_page = 3

N = 5
L = [2, 4, 2, 2, 3]

1 2 3 4 5 6 7
        |___|

a b | 1 2 3 4 5 6 7
|_________________|                    


"""
from typing import List
import math

def getMaxVisitableWebpages(N: int, L: List[int]) -> int:
  page_id = [0] * (N + 1)
  page_path = [0] * (N + 1)

  for page in range(1, N+1):
    if page_id[page] != 0:
      continue

    path_len, start_page = 0, page
    while page_id[page] == 0:
      path_len += 1
      page_path[page] = path_len
      page_id[page] = start_page
      page = L[page - 1]
    
    # dfs loops back into self
    if page_id[page] == start_page:
      page_cycle = path_len - page_path[page] + 1
      while page_id[page] != -start_page:
        page_path[page] = page_cycle
        page_id[page] = -start_page
        page = L[page - 1]
    
    else:
      path_len += page_path[page]
    
    page = start_page
    while page_id[page] == start_page:
      page_path[page] = path_len
      path_len -= 1
      page = L[page - 1]
  return max(page_path)

    
  
  
  
