import sys
sys.stdout.reconfigure(encoding='utf-8')

# test here


class DecisionTreeVisualizer:
    def __init__(self):
        self.step = 0

    def snapshot(self, message):
        self.step += 1
        print(f"\n===== SNAPSHOT {self.step} =====")
        print(f"Reason: {message}")

    def print_tree(self, path_stack):
        print("\nDecision Tree Path:")
        for depth, node in enumerate(path_stack):
            indent = "    " * depth
            connector = "└── " if depth > 0 else ""
            print(f"{indent}{connector}{node}")


class Solution:
    def addOperators(self, num: str, target: int):
        self.visualizer = DecisionTreeVisualizer()
        results = []

        self.visualizer.snapshot("Starting Decision Tree Exploration")

        self._backtrack(
            index=0,
            expression="",
            current_total=0,
            last_operand=0,
            num=num,
            target=target,
            results=results,
            path_stack=["ROOT"]
        )

        self.visualizer.snapshot("Finished exploring all branches")

        print("\n===== FINAL VALID EXPRESSIONS =====")
        print(results)

        return results

    def _backtrack(
        self,
        index,
        expression,
        current_total,
        last_operand,
        num,
        target,
        results,
        path_stack
    ):
        # Print current decision tree path
        self.visualizer.print_tree(path_stack)

        if index == len(num):
            self.visualizer.snapshot("Reached leaf node, evaluating expression")

            print(f"Expression: {expression} | Total: {current_total}")

            if current_total == target:
                print("✅ VALID EXPRESSION\n")
                results.append(expression)
            else:
                print("❌ Invalid expression\n")
            return

        for end in range(index, len(num)):
            current_str = num[index:end + 1]

            if len(current_str) > 1 and current_str[0] == '0':
                self.visualizer.snapshot("Pruned branch due to leading zero")
                continue

            current_number = int(current_str)

            # First number (root level)
            if index == 0:
                new_path = path_stack + [current_str]

                self.visualizer.snapshot("Choosing first number (root branch)")

                self._backtrack(
                    end + 1,
                    current_str,
                    current_number,
                    current_number,
                    num,
                    target,
                    results,
                    new_path
                )

            else:
                # Addition branch
                new_path = path_stack + [f"+{current_str}"]

                self.visualizer.snapshot("Branching with '+' operator")

                self._backtrack(
                    end + 1,
                    expression + "+" + current_str,
                    current_total + current_number,
                    current_number,
                    num,
                    target,
                    results,
                    new_path
                )

                # Subtraction branch
                new_path = path_stack + [f"-{current_str}"]

                self.visualizer.snapshot("Branching with '-' operator")

                self._backtrack(
                    end + 1,
                    expression + "-" + current_str,
                    current_total - current_number,
                    -current_number,
                    num,
                    target,
                    results,
                    new_path
                )

                # Multiplication branch
                new_total = current_total - last_operand + (last_operand * current_number)

                new_path = path_stack + [f"*{current_str}"]

                self.visualizer.snapshot("Branching with '*' operator (handling precedence)")

                self._backtrack(
                    end + 1,
                    expression + "*" + current_str,
                    new_total,
                    last_operand * current_number,
                    num,
                    target,
                    results,
                    new_path
                )


# ===== TEST EXECUTION =====

solution = Solution()
solution.addOperators("232", 8)