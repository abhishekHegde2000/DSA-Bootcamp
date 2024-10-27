'''
https://leetcode.com/problems/find-smallest-letter-greater-than-target/

744. Find Smallest Letter Greater Than Target

You are given an array of characters letters that is sorted in non-decreasing order, and a character target. There are at least two different characters in letters.

Return the smallest character in letters that is lexicographically greater than target. If such a character does not exist, return the first character in letters.



Example 1:

Input: letters = ["c","f","j"], target = "a"
Output: "c"
Explanation: The smallest character that is lexicographically greater than 'a' in letters is 'c'.
Example 2:

Input: letters = ["c","f","j"], target = "c"
Output: "f"
Explanation: The smallest character that is lexicographically greater than 'c' in letters is 'f'.
Example 3:

Input: letters = ["x","x","y","y"], target = "z"
Output: "x"
Explanation: There are no characters in letters that is lexicographically greater than 'z' so we return letters[0].
'''

'''


**Intuition:**

- **Key concept:** Efficiently locate the smallest lexicographically greater letter in a circular array of letters using binary search.
- **Circular nature:** Handle the circularity by wrapping around to the beginning if a greater letter isn't found within the initial range.

**Approach:**

1. **Initialize pointers:** Set `starting_index` to 0 and `ending_index` to the array's length minus 1.
2. **Iterate using binary search:**
   - Calculate the `middle_index`.
   - **Compare middle letter to target:**
      - If `letters[middle_index]` is greater than the target, store the potential answer and focus on the left half to find a closer greater letter.
      - Otherwise, update `starting_index` to `middle_index + 1` to search the right half.
3. **Handle wrap-around:** If a greater letter wasn't found within the initial range, wrap around to the first letter using the modulo operator.
4. **Return the answer:** Return the letter at the calculated index.

**Pseudocode:**

1. Initialize starting_index to 0 and ending_index to length of letters - 1
2. While starting_index is less than or equal to ending_index:
    a. Calculate middle_index as (starting_index + ending_index) divided by 2
    b. If letters[middle_index] is greater than target:
       - Store middle_index as potential answer
       - Update ending_index to middle_index - 1 to focus on left half
    c. Else:
       - Update starting_index to middle_index + 1 to search right half
3. Calculate wrapped_index using modulo operator to handle wrap-around
4. Return letters[wrapped_index]

**Complexity:**

- **Time complexity:** O(log n), due to binary search, where n is the number of letters.
- **Space complexity:** O(1), as it uses a constant amount of extra space.

**Code with comments and debugging prints:**

```python
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        starting_index = 0  # Initialize starting point of search
        ending_index = len(letters) - 1  # Initialize ending point of search
        potential_greater_letter_index = 0  # Initialize potential answer

        while starting_index <= ending_index:
            middle_index = (starting_index + ending_index) // 2

            print(f"Searching in range: {letters[starting_index:ending_index + 1]} "
                  f"(middle letter: {letters[middle_index]})")  # Debugging print

            if letters[middle_index] > target:
                potential_greater_letter_index = middle_index  # Store potential answer
                ending_index = middle_index - 1  # Focus on left half
            else:
                starting_index = middle_index + 1  # Search right half

        wrapped_index = potential_greater_letter_index % len(letters)  # Handle wrap-around
        return letters[wrapped_index]  # Return the smallest greater letter
```
'''

from typing import List
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        starting_index = 0  # Initialize starting point of search
        ending_index = len(letters) - 1  # Initialize ending point of search
        potential_greater_letter_index = 0  # Initialize potential answer

        while starting_index <= ending_index:
            middle_index = (starting_index + ending_index) // 2

            print(f"Searching in range: {letters[starting_index:ending_index + 1]} "
                  # Debugging print
                  f"(middle letter: {letters[middle_index]})")

            if letters[middle_index] > target:
                potential_greater_letter_index = middle_index  # Store potential answer
                ending_index = middle_index - 1  # Focus on left half
            else:
                starting_index = middle_index + 1  # Search right half

        wrapped_index = potential_greater_letter_index % len(
            letters)  # Handle wrap-around
        return letters[wrapped_index]  # Return the smallest greater letter
