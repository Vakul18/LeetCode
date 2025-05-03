"""
Here's your formatted and cleaned-up version of the problem description for clarity and readability:

---

### 🧙‍♂️ Problem Statement: Maximum Damage to the Boss

There are `N` warriors, each with their own health and damage stats:
- The `i-th` warrior has:
  - Health = `H[i]` units
  - Damage per second = `D[i]` units

They are up against a **boss** with:
- **Unlimited health**
- **Fixed damage per second**: `B`

---

### ⚔️ Battle Rules

- Damage is dealt **continuously** (e.g., in 0.5 seconds, the boss deals `B / 2` damage).
- **Only two warriors** will fight the boss: one in front, one as backup.
- The boss attacks **the front-line warrior (`i`)** until they are defeated (i.e., when `H[i]` damage has been dealt).
- Then the **backup warrior (`j`)** steps in and fights until they are also defeated.

**Both warriors deal damage to the boss while they are alive.**  
The total damage done is the sum of both warriors’ contributions during their survival time.

---

### 🎯 Goal

Find the **maximum total damage** that can be dealt to the boss for any choice of two different warriors (`i ≠ j`).

---

### 📌 Constraints

- `2 ≤ N ≤ 500,000`
- `1 ≤ H[i], D[i] ≤ 1,000,000,000`
- `1 ≤ B ≤ 1,000,000,000`
- Return value must have an **absolute or relative error** of at most `10⁻⁶`.

---

### 🧪 Sample Test Cases

#### Test Case #1
- `N = 3`
- `H = [2, 1, 4]`
- `D = [3, 1, 2]`
- `B = 4`
- ✅ Expected Output: `6.500000`

#### Test Case #2
- `N = 4`
- `H = [1, 1, 2, 100]`
- `D = [1, 2, 1, 3]`
- `B = 8`
- ✅ Expected Output: `62.750000`

#### Test Case #3
- `N = 4`
- `H = [1, 1, 2, 3]`
- `D = [1, 2, 1, 100]`
- `B = 8`
- ✅ Expected Output: `62.750000`

---

### 🧠 Sample Explanation (Case #1)

Warriors:
- Healths: `[2, 1, 4]`
- Damages: `[3, 1, 2]`
- Boss Damage: `B = 4`

Best combo:  
- Front: Warrior 3 (H=4, D=2)  
- Backup: Warrior 1 (H=2, D=3)

**Timeline:**
1. Warrior 3 survives for `4 / 4 = 1` second → deals `1 * 2 = 2` damage.
2. Warrior 1 deals `3` damage during this 1 second as backup.
3. Warrior 1 then takes the front line and survives for `2 / 4 = 0.5` seconds → deals `0.5 * 3 = 1.5` damage.

**Total Damage = 2 + 3 + 1.5 = 6.5 units**

Warriors:
- Healths: `[4, 6, 5, 8]`
- Damages: `[3, 2.2, 2.5, 2]`
- Boss Damage: `B = 4`
4 + 3 + 3 = 10
3.3 + 3.75 + 3.125= 10.
3.125 +  3.75 + 3

"""
"""
- Healths: `[49, 6, 5, 8]`
                     
- Damages: `[3, 2.2, 2.5, 2]`

Health: [8, 6, 5, 4]
Damage: [3,2.5, 2.2, 2]

"""

from typing import List
# Write any import statements here

def getMaxDamageDealt(N: int, H: List[int], D: List[int], B: int) -> float:
  C = [h * d for h, d in zip(H, D)]
  
  max_damage = 0
  best_warrior = 0
  
  run = True
  while run:
      run = False
      next_best_warrior = 0
    
      for i in range(N):
          if i == best_warrior:
              continue
        
          damage = C[best_warrior] + C[i] + max(H[best_warrior] * D[i], H[i] * D[best_warrior])
          if damage > max_damage:
              run = True
              max_damage = damage
              next_best_warrior = i
    
      best_warrior = next_best_warrior
    
  return max_damage / B









"""