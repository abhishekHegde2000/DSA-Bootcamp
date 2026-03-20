from typing import List
import sys
sys.stdout.reconfigure(encoding='utf-8')

# test here


class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        # Defensive check: if input is empty, return empty list
        if not num:
            return []

        results = []

        # I start DFS from index 0
        self._dfs(
            num=num,
            target=target,
            index=0,
            current_expression="",
            current_total=0,
            last_operand=0,
            results=results
        )

        return results

    def _dfs(self, num, target, index, current_expression, current_total, last_operand, results):
        # Base Case: All digits consumed
        if index == len(num):
            # Only expressions that evaluate exactly to target are valid
            if current_total == target:
                results.append(current_expression)
            return

        # Try all possible substrings starting at index
        for end in range(index, len(num)):
            # Avoid numbers with leading zero (e.g., "05" is invalid, but "0" is valid)
            if end > index and num[index] == '0':
                break

            # Extract current number string and convert to int
            current_str = num[index:end + 1]
            current_num = int(current_str)

            # CASE 1: First number (no operator before it)
            if index == 0:
                self._dfs(
                    num,
                    target,
                    end + 1,
                    current_str,
                    current_num,
                    current_num,
                    results
                )
            else:
                # CASE 2: Addition
                self._dfs(
                    num,
                    target,
                    end + 1,
                    current_expression + "+" + current_str,
                    current_total + current_num,
                    current_num,
                    results
                )

                # CASE 3: Subtraction
                self._dfs(
                    num,
                    target,
                    end + 1,
                    current_expression + "-" + current_str,
                    current_total - current_num,
                    -current_num,
                    results
                )

                # CASE 4: Multiplication (Handling precedence)
                # Formula: current_total - last_operand + (last_operand * current_num)
                new_total = current_total - last_operand + \
                    (last_operand * current_num)

                self._dfs(
                    num,
                    target,
                    end + 1,
                    current_expression + "*" + current_str,
                    new_total,
                    last_operand * current_num,
                    results
                )

# ------------------------------------------------------------------------------
# TEST RUN
# ------------------------------------------------------------------------------


sol = Solution()

# # Test Case 1: Standard case
# num_1, target_1 = "123", 6
# result_1 = sol.addOperators(num_1, target_1)
# print(f"Input: num='{num_1}', target={target_1} | Result: {result_1}")

# # Test Case 2: Handling multiplication precedence
# num_2, target_2 = "232", 8
# result_2 = sol.addOperators(num_2, target_2)
# print(f"Input: num='{num_2}', target={target_2} | Result: {result_2}")

# Test Case 3: Leading zeros (User Example)
num_3, target_3 = "105", 5
result_3 = sol.addOperators(num_3, target_3)
print(f"Input: num='{num_3}', target={target_3} | Result: {result_3}")

# # Test Case 4: No possible solution
# num_4, target_4 = "3456237490", 9191
# result_4 = sol.addOperators(num_4, target_4)
# print(f"Input: num='{num_4}', target={target_4} | Result: {result_4}")

# # Test Case 5: Edge Case - Single digit
# num_5, target_5 = "5", 5
# result_5 = sol.addOperators(num_5, target_5)
# print(f"Input: num='{num_5}', target={target_5} | Result: {result_5}")
