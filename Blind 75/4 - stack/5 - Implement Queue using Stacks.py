'''
https://leetcode.com/problems/implement-queue-using-stacks/description/?envType=daily-question&envId=2024-01-29

232. Implement Queue using Stacks

Implement a first in first out (FIFO) queue using only two stacks. The implemented queue should support all the functions of a normal queue (push, peek, pop, and empty).

Implement the MyQueue class:

void push(int x) Pushes element x to the back of the queue.
int pop() Removes the element from the front of the queue and returns it.
int peek() Returns the element at the front of the queue.
boolean empty() Returns true if the queue is empty, false otherwise.
Notes:

You must use only standard operations of a stack, which means only push to top, peek/pop from top, size, and is empty operations are valid.
Depending on your language, the stack may not be supported natively. You may simulate a stack using a list or deque (double-ended queue) as long as you use only a stack's standard operations.
 

Example 1:

Input
["MyQueue", "push", "push", "peek", "pop", "empty"]
[[], [1], [2], [], [], []]
Output
[null, null, null, 1, 1, false]

Explanation
MyQueue myQueue = new MyQueue();
myQueue.push(1); // queue is: [1]
myQueue.push(2); // queue is: [1, 2] (leftmost is front of the queue)
myQueue.peek(); // return 1
myQueue.pop(); // return 1, queue is [2]
myQueue.empty(); // return false
 

Constraints:

1 <= x <= 9
At most 100 calls will be made to push, pop, peek, and empty.
All the calls to pop and peek are valid.
 

Follow-up: Can you implement the queue such that each operation is amortized O(1) time complexity? In other words, performing n operations will take overall O(n) time even if one of those operations may take longer.


'''


class MyQueue:

    def __init__(self):
        self.input_stack = []  # Stack for pushing new elements
        self.output_stack = []  # Stack for popping and peeking elements

    def push(self, value: int) -> None:
        print(f"Pushing {value} to the queue")
        # Push the new element to the input stack
        self.input_stack.append(value)
        print(f"Input stack: {self.input_stack}")

    def pop(self) -> int:
        # If the output stack is empty, pop all elements from the input stack and push them to the output stack
        if not self.output_stack:
            print("Output stack is empty, transferring elements from input stack")
            while self.input_stack:
                self.output_stack.append(self.input_stack.pop())
            print(f"Output stack: {self.output_stack}")
        # Pop and return the top element from the output stack
        return self.output_stack.pop()

    def peek(self) -> int:
        # If the output stack is empty, pop all elements from the input stack and push them to the output stack
        if not self.output_stack:
            print("Output stack is empty, transferring elements from input stack")
            while self.input_stack:
                self.output_stack.append(self.input_stack.pop())
            print(f"Output stack: {self.output_stack}")
        # Return the top element from the output stack without popping it
        return self.output_stack[-1]

    def empty(self) -> bool:
        # The queue is empty if both stacks are empty
        return not self.input_stack and not self.output_stack


sol = MyQueue()

sol.push(1)
sol.push(2)
print(sol.peek())
print(sol.pop())
print(sol.empty())
