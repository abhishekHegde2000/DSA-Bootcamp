from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.

        ALGORITHM EXPLANATION:
        This uses the "Dutch National Flag" algorithm. We use three pointers to maintain three invariant sections:
        1. nums[0...low-1] are 0s (Red)
        2. nums[low...mid-1] are 1s (White)
        3. nums[high+1...end] are 2s (Blue)

        - 'mid' traverses the array.
        - If we see a 0, we swap it to the 'low' boundary and advance both 'low' and 'mid'.
        - If we see a 1, we just advance 'mid' (it's already in the correct relative zone).
        - If we see a 2, we swap it to the 'high' boundary and shrink 'high'. We do NOT advance 'mid' because the value swapped from 'high' is unknown and needs inspection.

        COMPLEXITY ANALYSIS:
        - Time Complexity: O(N). We traverse the array exactly once. Each element is visited at most by the 'mid' pointer.
        - Space Complexity: O(1). We sort in-place using only three integer variables for pointers.
        """
        low = 0
        mid = 0
        high = len(nums) - 1

        while mid <= high:
            if nums[mid] == 0:
                # Swap current 0 to the low boundary
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                # 1s are in the middle, just move forward
                mid += 1
            else: # nums[mid] == 2
                # Swap current 2 to the high boundary
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1

# ------------------------------------------------------------------------------
# TEST RUN
# ------------------------------------------------------------------------------

sol = Solution()

# Helper function to print test results cleanly
def run_test(test_name, input_nums, expected):
    print(f"--- {test_name} ---")
    print(f"Input:    {input_nums}")
    # Create a copy for verification since sortColors is in-place
    nums_copy = input_nums[:]
    sol.sortColors(nums_copy)
    print(f"Output:   {nums_copy}")
    print(f"Expected: {expected}")
    print(f"Status:   {'PASS' if nums_copy == expected else 'FAIL'}")
    print("")

# Test Case 1: Standard Mixed Input (LeetCode Example)
input_1 = [2, 0, 2, 1, 1, 0]
expected_1 = [0, 0, 1, 1, 2, 2]
run_test("Test Case 1 (Standard)", input_1, expected_1)

# Test Case 2: Edge Case - Only 2s and 0s
input_2 = [2, 0, 1]
expected_2 = [0, 1, 2]
run_test("Test Case 2 (Simple)", input_2, expected_2)

# Test Case 3: Edge Case - Already Sorted
input_3 = [0, 1, 2]
expected_3 = [0, 1, 2]
run_test("Test Case 3 (Already Sorted)", input_3, expected_3)

# Test Case 4: Edge Case - Reversed
input_4 = [2, 2, 1, 1, 0, 0]
expected_4 = [0, 0, 1, 1, 2, 2]
run_test("Test Case 4 (Reversed)", input_4, expected_4)

# Test Case 5: Single Element
input_5 = [1]
expected_5 = [1]
run_test("Test Case 5 (Single Element)", input_5, expected_5)

# Test Case 6: Uniform Array (All same)
input_6 = [2, 2, 2, 2]
expected_6 = [2, 2, 2, 2]
run_test("Test Case 6 (Uniform)", input_6, expected_6)
