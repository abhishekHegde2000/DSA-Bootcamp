
'''


---

**Title: Infinite Binary Tree Paths**

**Topics: Trees, Binary Tree, Recursion**

**Problem:**

Consider an infinite binary tree with the following structure:

- At each odd level, each node has two children.
- At each even level, each node has only one child.

The tree nodes have consecutive values starting from 1.

**Example:**

```
      1
     / \
    2   3
   /     \
  4       5
 / \     / \
6   7   8   9
```

Write a function `find_path(n: int) -> List[int]` that takes a node value `n` as input and returns the path from the given node to the root of the tree. The path should be a list of node values, starting from the given node and going up to the root.



**Example Test Cases:**

```python
# Test Case 1
assert find_path(7) == [1, 2, 4, 7], "Test Case 1 Failed"

# Test Case 2
assert find_path(5) == [1, 3, 5], "Test Case 2 Failed"

# Test Case 3
assert find_path(8) == [1, 3, 5, 8], "Test Case 3 Failed"
```

**Explanation:**

- For Test Case 1: The path from node 7 to the root is 7 -> 4 -> 2 -> 1.
- For Test Case 2: The path from node 5 to the root is 5 -> 3 -> 1.
- For Test Case 3: The path from node 8 to the root is 8 -> 5 -> 3 -> 1.

Your task is to implement the `find_path` function and ensure that it passes the provided test cases.

---

'''
from typing import List


def isEvenSublevel(startNode, level, x):
    evenRowSize = 2**level
    evenRowNode = startNode + evenRowSize
    if x < evenRowNode:
        return False
    return True


def getParent(x, level, isEven, startNode):
    if isEven:
        evenRowStartNode = startNode + (2**level)
        parentIndexInRow = (x - evenRowStartNode)/2
        parentNode = startNode + int(parentIndexInRow)
        return parentNode
    else:
        return x-(2**level)


def findPath(x):
    level = 0
    nodes = [1]  # it represents start node of each level

    # create the starting Node array
    while nodes[-1] <= x:
        node = nodes[-1]
        levelSize = 3*(2**level)
        nextNode = node+levelSize
        nodes.append(nextNode)
        level += 1

    # come back to level which contains X
    level = level-1
    nodes.pop()

    # check if X is in evenSublevel or Odd
    isEven = isEvenSublevel(nodes[-1], level, x)
    ans = [x]
    while x != 1:
        parent = getParent(x, level, isEven, nodes[-1])
        ans.append(parent)
        x = parent
        isEven = not isEven
        if isEven:
            level -= 1
            nodes.pop()
    return ans


print(findPath(26))  # [26, 18, 12, 8, 5, 3, 1]

print(findPath(17))  # [17, 11, 7, 4, 2, 1]

print(findPath(1))  # [1]


print(find_path(7))  # [1, 2, 4, 7]
print(find_path(5))  # [1, 3, 5]
print(find_path(8))  # [1, 3, 5, 8]
