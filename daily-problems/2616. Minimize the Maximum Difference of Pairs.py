'''

https://leetcode.com/problems/minimize-the-maximum-difference-of-pairs/

2616. Minimize the Maximum Difference of Pairs
Solved
Medium
Topics
premium lock icon
Companies
Hint
You are given a 0-indexed integer array nums and an integer p. Find p pairs of indices of nums such that the maximum difference amongst all the pairs is minimized. Also, ensure no index appears more than once amongst the p pairs.

Note that for a pair of elements at the index i and j, the difference of this pair is |nums[i] - nums[j]|, where |x| represents the absolute value of x.

Return the minimum maximum difference among all p pairs. We define the maximum of an empty set to be zero.



Example 1:

Input: nums = [10,1,2,7,1,3], p = 2
Output: 1
Explanation: The first pair is formed from the indices 1 and 4, and the second pair is formed from the indices 2 and 5.
The maximum difference is max(|nums[1] - nums[4]|, |nums[2] - nums[5]|) = max(0, 1) = 1. Therefore, we return 1.
Example 2:

Input: nums = [4,2,1,2], p = 1
Output: 0
Explanation: Let the indices 1 and 3 form a pair. The difference of that pair is |2 - 2| = 0, which is the minimum we can attain.


Constraints:

1 <= nums.length <= 105
0 <= nums[i] <= 109
0 <= p <= (nums.length)/2


'''


from typing import List


# brute force - TLE

class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        # Sorting helps us pair adjacent elements to minimize differences.
        nums.sort()
        n = len(nums)

        # Function to check if we can form at least p pairs with max difference <= threshold
        def can_form_pairs(threshold):
            count = 0
            i = 0
            while i < n - 1:
                if nums[i+1] - nums[i] <= threshold:
                    count += 1
                    i += 2  # Skip the next element as it's paired
                else:
                    i += 1  # Try the next element
            return count >= p

        # Brute-force: Try increasing thresholds starting from 0
        threshold = 0
        while True:
            if can_form_pairs(threshold):
                return threshold
            threshold += 1


# Optimized - Binary Search + greedy approach


class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        nums.sort()
        n = len(nums)

        # Greedy check: can we form at least p pairs with max difference <= max_diff?
        def can_form_pairs(max_diff):
            count = 0
            i = 0
            while i < n - 1:
                if nums[i + 1] - nums[i] <= max_diff:
                    count += 1
                    i += 2  # Skip the paired elements
                else:
                    i += 1  # Try the next possible element
            return count >= p

        # Binary search to minimize the maximum difference
        left = 0
        right = nums[-1] - nums[0]  # Maximum possible difference

        while left < right:
            mid = (left + right) // 2
            if can_form_pairs(mid):
                right = mid  # Try to minimize further
            else:
                left = mid + 1  # Increase the allowed difference

        return left


'''
This is an excellent question!
Let me walk you through the **step-by-step thought process** I would follow to arrive at this solution naturally, even without knowing it upfront.

---

# 🚀 How to Arrive at This Solution: Step-by-Step Thought Process

## 1. **Understand the Goal Clearly**

We are asked to:

* **Form exactly `p` pairs** from the array.
* **Minimize the largest difference** among the selected pairs.

So we need:

* A solution that can **check possible maximum differences efficiently.**

---

## 2. **Start with Intuition: Sort the Array**

When you need to minimize differences, **sorting is usually the first step** because:

* The smallest differences will always be between adjacent elements.

👉 This is a **key unlocking step.**

---

## 3. **Brute Force Trial (Your Initial Idea)**

It’s natural to think:

* Let’s try every possible threshold and see if we can make `p` pairs.

But while thinking through this:

* You realize this can be **too slow** because the difference range could be large.

---

## 4. **Look for Searchable Space: Can We Binary Search?**

Whenever you hear:

* **"Minimize the maximum"**
* **"Find the smallest threshold that satisfies a condition"**

🔥 These are huge signals that the problem can be solved with **Binary Search on the Answer.**

> *Why?*
> Because the answer is **monotonic**:
> If it is possible to make `p` pairs with difference ≤ `d`, it will also be possible with difference ≤ `d+1`, `d+2`, etc.

Monotonicity allows Binary Search to work!

---

## 5. **Design the Binary Search**

Now you need:

* A **lower bound**: Minimum possible difference (`0`)
* An **upper bound**: Maximum possible difference (`max(nums) - min(nums)`)

You can binary search in this range to find the smallest difference where it’s possible to form `p` pairs.

---

## 6. **Greedy Validation**

How to check if `p` pairs are possible for a given difference?

✅ Greedy strategy is ideal because:

* When you sort, you should always pair elements **as early as possible** (pair adjacent elements if their difference is small enough).

Why greedy works:

* Pairing the earliest elements leaves more flexibility later in the array to form remaining pairs.

👉 This is a **key DSA pattern:**

> When you are allowed to make selections under constraints and want to maximize or minimize something → Greedy often works.

---

## 7. **Binary Search + Greedy = Standard DSA Combo**

This combination is very common in:

* Array pairing problems
* Distance minimization problems
* Threshold finding problems

Once you spot that:

* The answer space is monotonic
* The feasibility check can be done in O(N)

It becomes a natural fit for **Binary Search on the Answer.**

---

# 🔁 Summary of the Thought Process:

| Step            | What to Ask Yourself                                                      |
| --------------- | ------------------------------------------------------------------------- |
| 1. Sort?        | Does minimizing a difference typically benefit from sorting? (Yes)        |
| 2. Brute Force  | Can I solve this by checking every possible answer? (Yes, but slow)       |
| 3. Search Space | Is the answer space ordered/monotonic? (Yes → Binary Search)              |
| 4. Greedy Check | How do I quickly verify a candidate answer? (Greedy pairing works)        |
| 5. Combine      | Can I combine Binary Search with Greedy validation? (Yes, standard combo) |

---

### 🚀 If You Practice:

The more problems you solve where **Binary Search on the Answer + Greedy Check** works,
👉 the faster you’ll naturally start seeing this path.

---

### 👉 I can help you:

* Find a few similar problems to practice this exact thought pattern.
* Guide you through a few more like this step-by-step until you start recognizing them automatically.

Let me know if you’d like me to suggest some good follow-up problems!

'''
