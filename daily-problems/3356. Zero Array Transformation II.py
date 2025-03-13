'''
https://leetcode.com/problems/zero-array-transformation-ii

3356. Zero Array Transformation II
Medium
Topics
Companies
Hint
You are given an integer array nums of length n and a 2D array queries where queries[i] = [li, ri, vali].

Each queries[i] represents the following action on nums:

Decrement the value at each index in the range [li, ri] in nums by at most vali.
The amount by which each value is decremented can be chosen independently for each index.
A Zero Array is an array with all its elements equal to 0.

Return the minimum possible non-negative value of k, such that after processing the first k queries in sequence, nums becomes a Zero Array. If no such k exists, return -1.



Example 1:

Input: nums = [2,0,2], queries = [[0,2,1],[0,2,1],[1,1,3]]

Output: 2

Explanation:

For i = 0 (l = 0, r = 2, val = 1):
Decrement values at indices [0, 1, 2] by [1, 0, 1] respectively.
The array will become [1, 0, 1].
For i = 1 (l = 0, r = 2, val = 1):
Decrement values at indices [0, 1, 2] by [1, 0, 1] respectively.
The array will become [0, 0, 0], which is a Zero Array. Therefore, the minimum value of k is 2.
Example 2:

Input: nums = [4,3,2,1], queries = [[1,3,2],[0,2,1]]

Output: -1

Explanation:

For i = 0 (l = 1, r = 3, val = 2):
Decrement values at indices [1, 2, 3] by [2, 2, 1] respectively.
The array will become [4, 1, 0, 0].
For i = 1 (l = 0, r = 2, val = 1):
Decrement values at indices [0, 1, 2] by [1, 1, 0] respectively.
The array will become [3, 0, 0, 0], which is not a Zero Array.


Constraints:

1 <= nums.length <= 105
0 <= nums[i] <= 5 * 105
1 <= queries.length <= 105
queries[i].length == 3
0 <= li <= ri < nums.length
1 <= vali <= 5



'''


'''

Approach Overview
Observation:
Each query
[
𝑙
,
𝑟
,
𝑣
]
[l,r,v] gives you a “budget” of at most
𝑣
v for each index in the interval
[
𝑙
,
𝑟
]
[l,r]. Since you can choose the decrement independently per index, the key is to ensure that for every index
𝑖
i, the total “budget” from all queries covering
𝑖
i is at least
nums
[
𝑖
]
nums[i].

Transformation of the Problem:
After processing the first
𝑘
k queries, index
𝑖
i can be decreased by at most:

capacity
[
𝑖
]
=
∑
𝑗
=
0
𝑘
−
1
1
{
𝑙
𝑗
≤
𝑖
≤
𝑟
𝑗
}
⋅
𝑣
𝑗
capacity[i]=
j=0
∑
k−1
​
 1
{l
j
​
 ≤i≤r
j
​
 }
​
 ⋅v
j
​

We need this capacity to be at least
nums
[
𝑖
]
nums[i] for every
𝑖
i.

Using a Difference Array for Efficiency:
To simulate the effect of a set of queries quickly (instead of updating each index one by one), use a difference array. For each query
[
𝑙
,
𝑟
,
𝑣
]
[l,r,v], update:

diff[l] += v
If
𝑟
+
1
r+1 is within bounds, do diff[r+1] -= v
Then, the prefix sum of this difference array gives the cumulative decrement capacity at each index.

Binary Search for the Minimum
𝑘
k:
Since the queries are applied in order, you can binary search over
𝑘
k (from 0 to the total number of queries) to find the minimum
𝑘
k that makes every index’s cumulative capacity at least as large as the corresponding value in nums.

Edge Cases:

If nums is already a zero array, return 0.
If even after all queries the condition is not met, return -1.

'''


'''
Below is one way to approach the problem. I won’t give you the “final answer” directly; instead, I’ll outline a strategy and a sample implementation with comments. You can use this explanation to compare with your own work and let me know if you have questions or need further clarifications.

---

### **Approach Overview**

1. **Observation:**
   Each query \( [l, r, v] \) gives you a “budget” of at most \( v \) for each index in the interval \([l, r]\). Since you can choose the decrement independently per index, the key is to ensure that for every index \( i \), the total “budget” from all queries covering \( i \) is at least \( \text{nums}[i] \).

2. **Transformation of the Problem:**
   After processing the first \( k \) queries, index \( i \) can be decreased by at most:
   \[
   \text{capacity}[i] = \sum_{j=0}^{k-1} \mathbf{1}_{\{l_j \leq i \leq r_j\}} \cdot v_j
   \]
   We need this capacity to be at least \( \text{nums}[i] \) for every \( i \).

3. **Using a Difference Array for Efficiency:**
   To simulate the effect of a set of queries quickly (instead of updating each index one by one), use a difference array. For each query \([l, r, v]\), update:
   - `diff[l] += v`
   - If \( r + 1 \) is within bounds, do `diff[r+1] -= v`

   Then, the prefix sum of this difference array gives the cumulative decrement capacity at each index.

4. **Binary Search for the Minimum \( k \):**
   Since the queries are applied in order, you can binary search over \( k \) (from 0 to the total number of queries) to find the minimum \( k \) that makes every index’s cumulative capacity at least as large as the corresponding value in `nums`.

5. **Edge Cases:**
   - If `nums` is already a zero array, return 0.
   - If even after all queries the condition is not met, return -1.

---

### **Sample Implementation with Detailed Comments**

```python
class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums)
        q = len(queries)

        # Helper function: Given a candidate number of queries 'k',
        # this function checks if processing the first k queries
        # can yield enough "budget" for each index.
        def can_zero(k: int) -> bool:
            # Create a difference array of size n+1 (for efficient range updates)
            diff = [0] * (n + 1)

            # Process the first k queries and update the difference array
            for j in range(k):
                l, r, v = queries[j]
                diff[l] += v
                if r + 1 < n:
                    diff[r + 1] -= v

            # Convert the difference array to the cumulative capacity array
            current = 0
            for i in range(n):
                current += diff[i]
                # If at any index, the capacity is less than the required value,
                # then we cannot turn this index to 0.
                if current < nums[i]:
                    return False
            return True

        # Check if nums is already a zero array.
        if all(x == 0 for x in nums):
            return 0

        # Binary search over the range of queries (from 0 to q)
        left, right = 0, q + 1  # right is set to q+1 for a "not found" sentinel

        # Binary search to find the minimal k
        while left < right:
            mid = (left + right) // 2
            if can_zero(mid):
                right = mid  # mid queries are enough; try to see if we can do with fewer
            else:
                left = mid + 1  # mid queries are not enough; try with more queries

        # If left is within the number of queries, then we found a valid k.
        # Otherwise, return -1 indicating it's impossible.
        return left if left <= q else -1
```

---

### **Explanation of Key Steps:**

- **Difference Array Technique:**
  Instead of updating every index in \([l, r]\) directly (which would be too slow), we update a difference array. After processing the queries, a simple prefix sum gives us the total available decrement at each index.

- **Binary Search:**
  By checking if the first \( k \) queries are sufficient (using the `can_zero` helper function), we can binary search for the minimal \( k \). This turns a potential \( O(q \times n) \) simulation into \( O(\log q \times (q + n)) \), which is efficient for the given constraints.

- **Edge Cases:**
  Always check for cases like an already zero array or when even all queries cannot zero out the array.

---

Feel free to run through this code, test with various examples, and let me know if you have any questions about any part of the process. We can discuss potential improvements or alternatives if needed!
'''


class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums)
        q = len(queries)

        # Helper function: Given a candidate number of queries 'k',
        # this function checks if processing the first k queries
        # can yield enough "budget" for each index.
        def can_zero(k: int) -> bool:
            # Create a difference array of size n+1 (for efficient range updates)
            diff = [0] * (n + 1)

            # Process the first k queries and update the difference array
            for j in range(k):
                l, r, v = queries[j]
                diff[l] += v
                if r + 1 < n:
                    diff[r + 1] -= v

            # Convert the difference array to the cumulative capacity array
            current = 0
            for i in range(n):
                current += diff[i]
                # If at any index, the capacity is less than the required value,
                # then we cannot turn this index to 0.
                if current < nums[i]:
                    return False
            return True

        # Check if nums is already a zero array.
        if all(x == 0 for x in nums):
            return 0

        # Binary search over the range of queries (from 0 to q)
        left, right = 0, q + 1  # right is set to q+1 for a "not found" sentinel

        # Binary search to find the minimal k
        while left < right:
            mid = (left + right) // 2
            if can_zero(mid):
                right = mid  # mid queries are enough; try to see if we can do with fewer
            else:
                left = mid + 1  # mid queries are not enough; try with more queries

        # If left is within the number of queries, then we found a valid k.
        # Otherwise, return -1 indicating it's impossible.
        return left if left <= q else -1
