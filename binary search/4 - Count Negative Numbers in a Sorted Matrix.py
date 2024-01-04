'''

1351. Count Negative Numbers in a Sorted Matrix


Example 1:

Input: grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
Output: 8
Explanation: There are 8 negatives number in the matrix.
Example 2:

Input: grid = [[3,2],[1,0]]
Output: 0
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 100
-100 <= grid[i][j] <= 100
 

Follow up: Could you find an O(n + m) solution?

'''


class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        def count_negatives_in_row(row: List[int]) -> int:
            start_index = 0  # Initialize starting point of search
            end_index = len(row) - 1  # Initialize ending point of search

            while start_index <= end_index:
                middle_index = (start_index + end_index) // 2

                print(f"Searching in row: {row[start_index:end_index + 1]} "
                      # Debugging print
                      f"(middle value: {row[middle_index]})")

                if row[middle_index] < 0:
                    end_index = middle_index - 1  # Focus search on left half
                else:
                    start_index = middle_index + 1  # Search right half

            # Count negative numbers from end_index to the end
            return len(row) - end_index

        total_negative_count = 0
        for row in grid:
            negative_count_in_row = count_negatives_in_row(row)
            total_negative_count += negative_count_in_row
            print(f"Negative count in row: {
                  negative_count_in_row}")  # Debugging print

        return total_negative_count


'''
**Here's the rewritten code with explanations, intuition, approach, pseudocode, and complexity analysis:**

**Intuition:**

- **Key concept:** Count negative numbers efficiently in a 2D grid by utilizing binary search within each row.
- **Sorted rows:** Exploit the fact that each row is sorted in non-decreasing order to apply binary search.

**Approach:**

1. **Define a helper function for binary search:**
   - Perform binary search on a row to find the first negative number's index.
   - If no negative number is found, return the row's length (all numbers are non-negative).
2. **Iterate through rows:**
   - For each row in the grid, apply the binary search helper function to count its negative numbers.
3. **Sum the counts:** Accumulate the counts from each row to obtain the total negative numbers.

**Pseudocode:**

1. Define function count_negatives_in_row(row):
   a. Initialize start_index to 0 and end_index to length of row - 1
   b. While start_index is less than or equal to end_index:
      - Calculate middle_index as (start_index + end_index) divided by 2
      - If row[middle_index] is negative:
         - Update end_index to middle_index - 1 to focus on the left half
      - Else:
         - Update start_index to middle_index + 1 to search the right half
   c. Return length of row - end_index (number of negative numbers)
2. Initialize total_negative_count to 0
3. For each row in grid:
   a. Add count_negatives_in_row(row) to total_negative_count
4. Return total_negative_count

**Complexity:**

- **Time complexity:** O(m log n), where m is the number of rows and n is the average number of elements per row.
   - Binary search within each row takes O(log n) time.
- **Space complexity:** O(1), as it uses a constant amount of extra space.

**Code with comments and debugging prints:**

```python
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        def count_negatives_in_row(row: List[int]) -> int:
            start_index = 0  # Initialize starting point of search
            end_index = len(row) - 1  # Initialize ending point of search

            while start_index <= end_index:
                middle_index = (start_index + end_index) // 2

                print(f"Searching in row: {row[start_index:end_index + 1]} "
                      f"(middle value: {row[middle_index]})")  # Debugging print

                if row[middle_index] < 0:
                    end_index = middle_index - 1  # Focus search on left half
                else:
                    start_index = middle_index + 1  # Search right half

            return len(row) - end_index  # Count negative numbers from end_index to the end

        total_negative_count = 0
        for row in grid:
            negative_count_in_row = count_negatives_in_row(row)
            total_negative_count += negative_count_in_row
            print(f"Negative count in row: {negative_count_in_row}")  # Debugging print

        return total_negative_count
```

'''
