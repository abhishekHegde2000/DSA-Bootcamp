'''
# Design a Double-ended Queue (Deque)

https://github.com/kuroxx/dsa/blob/43ee631f61b4100c88d198f30919444373b33cb6/python3/0-data_structure/implementations/doubly_linked_list.py#L4

https: // neetcode.io/problems/queue

# Problem Statement
You are required to design and implement a Double-ended Queue(Deque) class that supports the following operations in O(1) time complexity:

- `isEmpty() -> bool`: Returns `true` if the deque is empty, otherwise returns `false`.
- `append(value: int) -> None`: Adds `value` to the end of the deque.
- `appendleft(value: int) -> None`: Adds `value` to the beginning of the deque.
- `pop() -> int`: Removes and returns the value at the end of the deque. Returns `-1` if the deque is empty.
- `popleft() -> int`: Removes and returns the value at the beginning of the deque. Returns `-1` if the deque is empty.

# Constraints
- All operations must be implemented in O(1) time complexity.
- You may assume that all input values are valid integers.

# Example
Consider the following sequence of operations and the corresponding expected outputs:

```python
# Initialize the deque
deque = Deque()

# Test isEmpty on an empty deque
print(deque.isEmpty())  # Output: True

# Append 10 to the deque
deque.append(10)

# Test isEmpty after append
print(deque.isEmpty())  # Output: False

# Append 20 to the left of the deque
deque.appendleft(20)

# Pop from the left of the deque
print(deque.popleft())  # Output: 20

# Pop from the deque
print(deque.pop())  # Output: 10

# Pop from an empty deque
print(deque.pop())  # Output: -1

# Append 30 to the deque
deque.append(30)

# Pop from the deque
print(deque.pop())  # Output: 30

# Test isEmpty after all pops
print(deque.isEmpty())  # Output: True
```

# Class Definition
```python

'''


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class Deque:
    def __init__(self):
        # Create two dummy nodes and link them
        self.head = Node(-1)
        self.tail = Node(-1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def isEmpty(self) -> bool:
        return self.head.next == self.tail

    def append(self, value) -> None:
        new_node = Node(value)
        last_node = self.tail.prev

        last_node.next = new_node
        new_node.prev = last_node
        new_node.next = self.tail
        self.tail.prev = new_node

    def appendleft(self, value) -> None:
        new_node = Node(value)
        first_node = self.head.next

        self.head.next = new_node
        new_node.prev = self.head
        new_node.next = first_node
        first_node.prev = new_node

    def pop(self) -> int:
        if self.isEmpty():
            return -1
        last_node = self.tail.prev
        value = last_node.value
        prev_node = last_node.prev

        prev_node.next = self.tail
        self.tail.prev = prev_node

        return value

    def popleft(self) -> int:
        if self.isEmpty():
            return -1
        first_node = self.head.next
        value = first_node.value
        next_node = first_node.next

        self.head.next = next_node
        next_node.prev = self.head

        return value
