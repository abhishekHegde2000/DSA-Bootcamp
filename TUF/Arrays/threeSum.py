from typing import List

class Solution:
    """
    Class to find all unique triplets in an array that sum up to zero.
    """
    def threeSum(self, numbers: List[int]) -> List[List[int]]:
        """
        Finds all unique triplets in the list `numbers` which give the sum of zero.

        Args:
            numbers: A list of integers.

        Returns:
            A list of lists, where each inner list is a unique triplet that sums to zero.
        """
        print(f"--- Function Call: threeSum({numbers}) ---")
        
        # [Input/Setup] Initialize variables and sort the input array
        result_triplets = []
        num_count = len(numbers)
        step_counter = 0

        # Sorting is crucial for the two-pointer approach and for skipping duplicates.
        numbers.sort()
        print(f"[Setup] Sorted numbers: {numbers}")

        # The main loop iterates through the array to fix the first element of a potential triplet.
        for i in range(num_count):
            step_counter += 1
            print(f"\n[Step {step_counter}] === Outer Loop: Fixing first element, index i = {i}, value = {numbers[i]} ===")

            # [Conditionals] Skip duplicate fixed elements to avoid duplicate triplets.
            if i > 0 and numbers[i] == numbers[i - 1]:
                print(f" → Condition met: numbers[{i}] ({numbers[i]}) == numbers[{i-1}] ({numbers[i-1]}). Skipping duplicate.")
                continue

            # [Setup] Initialize two pointers, one at the element after i and one at the end.
            left_pointer = i + 1
            right_pointer = num_count - 1
            print(f" → Initializing two pointers: left = {left_pointer}, right = {right_pointer}")

            # The inner loop uses two pointers to find the other two elements.
            while left_pointer < right_pointer:
                step_counter += 1
                print(f"\n[Step {step_counter}] -- Inner Loop --")
                print(f"   - Pointers: left = {left_pointer} (value={numbers[left_pointer]}), right = {right_pointer} (value={numbers[right_pointer]})")
                
                current_sum = numbers[i] + numbers[left_pointer] + numbers[right_pointer]
                print(f"   - Calculating sum: {numbers[i]} + {numbers[left_pointer]} + {numbers[right_pointer]} = {current_sum}")

                # [Conditionals] Adjust pointers based on the sum.
                if current_sum < 0:
                    print(f"   → Condition: Sum ({current_sum}) is less than 0. Moving left pointer forward to increase sum.")
                    left_pointer += 1
                elif current_sum > 0:
                    print(f"   → Condition: Sum ({current_sum}) is greater than 0. Moving right pointer backward to decrease sum.")
                    right_pointer -= 1
                else:
                    # [Updates] A triplet is found!
                    print(f"   → Condition: Sum is 0. Found a valid triplet!")
                    found_triplet = [numbers[i], numbers[left_pointer], numbers[right_pointer]]
                    result_triplets.append(found_triplet)
                    print(f"   → [Update] Added {found_triplet} to results. Current results: {result_triplets}")

                    # Move both pointers inward.
                    left_pointer += 1
                    right_pointer -= 1
                    
                    # [Conditionals] Skip duplicates for the left and right pointers.
                    while left_pointer < right_pointer and numbers[left_pointer] == numbers[left_pointer - 1]:
                        print(f"     → Skipping duplicate on the left side. New left pointer: {left_pointer + 1}")
                        left_pointer += 1
                    while left_pointer < right_pointer and numbers[right_pointer] == numbers[right_pointer + 1]:
                        print(f"     → Skipping duplicate on the right side. New right pointer: {right_pointer - 1}")
                        right_pointer -= 1

        # [Final Output] Return the list of unique triplets.
        print(f"\n[Result] Finished processing. Final list of triplets is: {result_triplets}")
        print("------------------------------------------\n")
        return result_triplets

### Test Case Execution

# Instantiate the solution class
solver = Solution()

# --- Test Case 1: Standard case with multiple solutions ---
print("===== TEST CASE 1 =====")
test_case_1 = [-1, 0, 1, 2, -1, -4]
final_result_1 = solver.threeSum(test_case_1)
print(f"✅ Final Answer for {test_case_1}: {final_result_1}")
print("=======================\n")

# --- Test Case 2: Array with no solution ---
print("===== TEST CASE 2 =====")
test_case_2 = [1, 2, 3, 4]
final_result_2 = solver.threeSum(test_case_2)
print(f"✅ Final Answer for {test_case_2}: {final_result_2}")
print("=======================\n")

# --- Test Case 3: Array with many duplicates and zeros ---
print("===== TEST CASE 3 =====")
test_case_3 = [0, 0, 0, 0]
final_result_3 = solver.threeSum(test_case_3)
print(f"✅ Final Answer for {test_case_3}: {final_result_3}")
print("=======================\n")

# --- Test Case 4: Array with positive and negative duplicates ---
print("===== TEST CASE 4 =====")
test_case_4 = [-2, 0, 0, 2, 2]
final_result_4 = solver.threeSum(test_case_4)
print(f"✅ Final Answer for {test_case_4}: {final_result_4}")
print("=======================\n")