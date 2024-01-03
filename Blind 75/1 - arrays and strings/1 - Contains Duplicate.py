'''

Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

 

Example 1:

Input: nums = [1,2,3,1]
Output: true
Example 2:

Input: nums = [1,2,3,4]
Output: false
Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true

'''


''' 5 approaches 

Sure, here are the five different approaches to solve the problem:

1. **Brute Force**
```python
def containsDuplicate(self, nums: List[int]) -> bool:
    n = len(nums)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if nums[i] == nums[j]: return True
    return False
```

2. **Sorting**
```python
def containsDuplicate(self, nums: List[int]) -> bool:
    nums.sort()
    for i in range(len(nums)-1):
        if nums[i] == nums[i+1]: return True
    return False
```

3. **Using Counter Function**
```python
from collections import Counter

def containsDuplicate(self, nums: List[int]) -> bool:
    freq = Counter(nums)
    for num, freq in freq.items():
        if freq > 1:
            return True
    return False
```

4. **Using Hashmap**
```python
def containsDuplicate(self, nums: List[int]) -> bool:
    counter = {}
    for num in nums:
        if num not in counter:
            counter[num] = 0
        counter[num] += 1
    for num, freq in counter.items():
        if freq > 1:
            return True
    return False
```

5. **Using Set**
```python
def containsDuplicate(self, nums: List[int]) -> bool:
    return len(set(nums)) != len(nums)
```

Please note that the time complexity and space complexity vary for each approach. The brute force approach has a time complexity of O(n^2) and space complexity of O(1). The sorting approach has a time complexity of O(n log n) and space complexity of O(1). The Counter function and hashmap approaches have a time complexity of O(n) and space complexity of O(n). The set approach has a time complexity of O(n) and space complexity of O(n).

'''




from typing import List
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)


sol = Solution()
print(sol.containsDuplicate([1, 2, 3, 1]))
print(sol.containsDuplicate([1, 2, 3, 4]))
