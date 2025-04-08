"""
Given a list of accounts where each element accounts[i] is a list of strings, where the first element accounts[i][0] is a name, and the rest of the elements are emails representing emails of the account.

Now, we would like to merge these accounts. Two accounts definitely belong to the same person if there is some common email to both accounts. Note that even if two accounts have the same name, they may belong to different people as people could have the same name. A person can have any number of accounts initially, but all of their accounts definitely have the same name.

After merging the accounts, return the accounts in the following format: the first element of each account is the name, and the rest of the elements are emails in sorted order. The accounts themselves can be returned in any order.

Input: accounts = [["John","johnsmith@mail.com","john_newyork@mail.com"],
["John","johnsmith@mail.com","john00@mail.com"],
["Mary","mary@mail.com"],
["John","johnnybravo@mail.com"]]
Output: [["John","john00@mail.com","john_newyork@mail.com","johnsmith@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]

accounts

name_set

1. iterate over all accs
1.1 check if name already exists
1.2 if not then add the list to res
1.3 if yes then 

"""
class DisjointSet:
  def __init__(self, n):
    self.parent = [i for i in range(n)]
    self.rank = [0] * n

  def findParent(self, u):
    if self.parent[u] == u:
      return u
    self.parent[u] = self.findParent(self.parent[u])
    return self.parent[u]

  def union(self, u, v):
    pu = self.findParent(u)
    pv = self.findParent(v)

    if pu == pv:
      return

    if self.rank[pu] > self.rank[pv]:
      self.parent[pv] = pu
    elif self.rank[pv] > self.rank[pu]:
      self.parent[pu] = pv
    else:
      self.parent[pv] = pu
      self.rank[pu] += 1

class Solution:
  def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
    n = len(accounts)
    ds = DisjointSet(n)
    idx_email = dict()

    for i in range(n): 
      account = accounts[i]
      for j in range(1, len(account)):
        if account[j] in idx_email:
          ds.union(i, idx_email[account[j]])
        else:
          idx_email[account[j]] = i
    
    merged_accounts = [[] for _ in range(n)]
    for index,(email,acc) in enumerate(idx_email.items()):
      parent = ds.findParent(acc)
      merged_accounts[parent].append(email)
    
    result = []
    for merged_acc in merged_accounts:
      if len(merged_acc) == 0 :
        continue
      sorted_list = sorted(merged_acc)
      acc_name = accounts[ds.findParent(idx_email[sorted_list[0]])][0]
      new_list = [acc_name] + sorted_list
      result.append(new_list)
    return result

---------------------------------------
class DisjointSet:
  def __init__(self, n):
    self.parent = [i for i in range(n)]
    self.rank = [0] * n

  def findParent(self, u):
    if self.parent[u] == u:
      return u
    self.parent[u] = self.findParent(self.parent[u])
    return self.parent[u]

  def union(self, u, v):
    pu = self.parent[u]
    pv = self.parent[v]

    if pu == pv:
      return

    if self.rank[pu] > self.rank[pv]:
      self.parent[pv] = pu
    elif self.rank[pv] > self.rank[pu]:
      self.parent[pu] = pv
    else:
      self.parent[pv] = pu
      self.rank[pu] += 1

class Solution: # wrong solution
  def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
    idx_email = dict()
    curr_idx = 0
    for account in accounts:
      for idx in range(1, len(account)):
        email = account[idx]
        if email not in idx_email:
          idx_email[email] = curr_idx 
          curr_idx += 1
    
    ds = DisjointSet(curr_idx+1)
    for account in accounts:
      u = idx_email[account[1]]
      for idx in range(2, len(account)):
        v = idx_email[account[idx]]
        ds.union(u, v)

    n = len(accounts)
    merged_accounts = []
    merged = [False] * n
    for i in range(n):
      if merged[i]:
        continue
      account = accounts[i][:]
      u = idx_email[account[1]]
      for j in range(i+1, n):
        v = idx_email[accounts[j][1]]
        if  ds.findParent(u) == ds.findParent(v):
          merged[j] = True
          account.extend(accounts[j][1:])
      merged_accounts.append(account)

    sorted_list_of_lists = []
    for inner_list in merged_accounts:
      if len(inner_list) > 1:
        first_element = inner_list[0]
        rest_of_list = sorted(inner_list[1:])
        sorted_list_of_lists.append([first_element] + rest_of_list)
      else:
        # If the inner list has 0 or 1 element, no sorting needed
        sorted_list_of_lists.append(inner_list[:])  # Append a copy
    
    return sorted_list_of_lists
        
        
        
