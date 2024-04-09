'''

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:

MinStack() initializes the stack object.
void push(int val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.
You must implement a solution with O(1) time complexity for each function.

 

Example 1:

Input
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

Output
[null,null,null,null,-3,null,0,-2]

Explanation
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // return -3
minStack.pop();
minStack.top();    // return 0
minStack.getMin(); // return -2

'''


'''
 **Here's the rewritten code with explanations, intuition, approach, pseudo code, and complexity:**

**# Intuition**

- **Key idea:** Use two stacks to track both values and their corresponding minimum values efficiently.
- **Stack for values:** Stores all pushed values.
- **Stack for minimums:** Stores the current minimum value at each point in time.

**# Approach**

1. **Initialize two empty stacks:**
   - `main_stack` to store all pushed values.
   - `minimum_value_stack` to store the current minimum value.
2. **Push:**
   - Add the value to `main_stack`.
   - Update `minimum_value_stack` with the minimum of the new value and the current minimum.
3. **Pop:**
   - Remove the top value from both stacks.
4. **Top:**
   - Return the top value from `main_stack`.
5. **GetMin:**
   - Return the top value from `minimum_value_stack` (the current minimum).

**# Pseudo Code**

```
1. Initialize main_stack = [], minimum_value_stack = []
2. push(val):
    a. main_stack.append(val)
    b. minimum_value_stack.append(min(minimum_value_stack[-1], val))
3. pop():
    a. main_stack.pop()
    b. minimum_value_stack.pop()
4. top():
    a. Return main_stack[-1]
5. getMin():
    a. Return minimum_value_stack[-1]
```

**# Complexity**

- **Time complexity:**
   - All operations (push, pop, top, getMin) take O(1) time, as they involve constant-time operations on stacks.
- **Space complexity:**
   - O(n), where n is the number of elements in the stack, as both stacks can potentially store all pushed elements.

**# Code with Debugging Print Statements and Comments**

```python
class MinStack:

    def __init__(self):
        self.main_stack = []  # Stack to store all values
        self.minimum_value_stack = []  # Stack to store the current minimum value

    def push(self, value: int) -> None:
        print(f"Pushing value: {value}")
        self.main_stack.append(value)
        if self.minimum_value_stack:
            updated_minimum = min(self.minimum_value_stack[-1], value)
            print(f"Updating minimum value to: {updated_minimum}")
            self.minimum_value_stack.append(updated_minimum)
        else:
            print(f"Initializing minimum value to: {value}")
            self.minimum_value_stack.append(value)

    def pop(self) -> None:
        print("Popping values from both stacks")
        self.main_stack.pop()
        self.minimum_value_stack.pop()

    def top(self) -> int:
        print(f"Returning top value: {self.main_stack[-1]}")
        return self.main_stack[-1]

    def getMin(self) -> int:
        print(f"Returning current minimum value: {self.minimum_value_stack[-1]}")
        return self.minimum_value_stack[-1]
```

'''


class MinStack:

    def __init__(self):
        self.main_stack = []  # Stack to store all values
        self.minimum_value_stack = []  # Stack to store the current minimum value

    def push(self, value: int) -> None:
        print(f"Pushing value: {value}")
        self.main_stack.append(value)
        if self.minimum_value_stack:
            updated_minimum = min(self.minimum_value_stack[-1], value)
            print(f"Updating minimum value to: {updated_minimum}")
            self.minimum_value_stack.append(updated_minimum)
        else:
            print(f"Initializing minimum value to: {value}")
            self.minimum_value_stack.append(value)

    def pop(self) -> None:
        print("Popping values from both stacks")
        self.main_stack.pop()
        self.minimum_value_stack.pop()

    def top(self) -> int:
        print(f"Returning top value: {self.main_stack[-1]}")
        return self.main_stack[-1]

    def getMin(self) -> int:
        print(
            f"Returning current minimum value: {self.minimum_value_stack[-1]}")
        return self.minimum_value_stack[-1]
