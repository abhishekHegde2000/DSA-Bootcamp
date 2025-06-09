'''

https://leetcode.com/problems/using-a-robot-to-print-the-lexicographically-smallest-string/

2434. Using a Robot to Print the Lexicographically Smallest String
Solved
Medium
Topics
premium lock icon
Companies
Hint
You are given a string s and a robot that currently holds an empty string t. Apply one of the following operations until s and t are both empty:

Remove the first character of a string s and give it to the robot. The robot will append this character to the string t.
Remove the last character of a string t and give it to the robot. The robot will write this character on paper.
Return the lexicographically smallest string that can be written on the paper.



Example 1:

Input: s = "zza"
Output: "azz"
Explanation: Let p denote the written string.
Initially p="", s="zza", t="".
Perform first operation three times p="", s="", t="zza".
Perform second operation three times p="azz", s="", t="".
Example 2:

Input: s = "bac"
Output: "abc"
Explanation: Let p denote the written string.
Perform first operation twice p="", s="c", t="ba".
Perform second operation twice p="ab", s="c", t="".
Perform first operation p="ab", s="", t="c".
Perform second operation p="abc", s="", t="".
Example 3:

Input: s = "bdda"
Output: "addb"
Explanation: Let p denote the written string.
Initially p="", s="bdda", t="".
Perform first operation four times p="", s="", t="bdda".
Perform second operation four times p="addb", s="", t="".


Constraints:

1 <= s.length <= 105
s consists of only English lowercase letters.

'''

from collections import Counter


class Solution:
    def robotWithString(self, s: str) -> str:
        cnt = Counter(s)
        stack = []
        res = []
        minCharacter = "a"
        for c in s:
            stack.append(c)
            cnt[c] -= 1
            while minCharacter != "z" and cnt[minCharacter] == 0:
                minCharacter = chr(ord(minCharacter) + 1)
            while stack and stack[-1] <= minCharacter:
                res.append(stack.pop())
        return "".join(res)


sol = Solution()

print(sol.robotWithString("zza"))  # "azz"
print(sol.robotWithString("bac"))  # "abc"
print(sol.robotWithString("bdda"))  # "addb"


'''
Great! You've found another **efficient and elegant greedy solution** to this problem using a `Counter`, a `stack`, and a dynamic `minCharacter`. Let's break it down **step-by-step with deep intuition** — **why** it works and how it's equivalent to the suffix-min idea but more space-efficient.

---

## 🔁 High-Level Recap of Problem:

* You can **push one character at a time** from `s` into a robot's stack `t`.
* You can **pop the last character from the stack** at any time and append to the output.
* Your goal is to construct the **lexicographically smallest** output string.

---

## 🔍 Key Components in Your Code:

```python
cnt = Counter(s)
stack = []
res = []
minCharacter = "a"
```

### ✅ Why `cnt = Counter(s)`?

* You use `cnt` to **track how many of each character are still left** in `s` as you iterate.
* This helps you determine the **smallest character that still exists** in the remaining part of `s`.

---

### ✅ Why `minCharacter = "a"`?

* You're simulating the **minimum character yet to come**, but instead of precomputing it like in `min_suffix[]`, you're **maintaining it dynamically**.
* `minCharacter` always tells you:
  **“What is the smallest possible character that still exists in `s` from this point forward?”**

---

## 🔁 The Main Loop Logic:

### 1. `stack.append(c)`

* You simulate pushing the current character from `s` into the robot's stack `t`.

### 2. `cnt[c] -= 1`

* You're removing this character from the frequency map — it’s no longer part of the “future.”

---

### 3. Update `minCharacter`

```python
while minCharacter != "z" and cnt[minCharacter] == 0:
    minCharacter = chr(ord(minCharacter) + 1)
```

**Purpose:** Keep bumping `minCharacter` forward until you find the **next smallest char** that is **still available** in `s`.

✅ Example:
Let’s say you processed all `'a'`, `'b'`, and `'c'`. Then `cnt['a'] == cnt['b'] == cnt['c'] == 0`.
So `minCharacter` becomes `'d'`.

This line **simulates** the logic of `min_suffix[i]` but does it **on-the-fly**.

---

### 4. Main Greedy Logic:

```python
while stack and stack[-1] <= minCharacter:
    res.append(stack.pop())
```

* This is the heart of the algorithm.
* If the character at the **top of the stack** is **≤ the smallest character left in `s`**, it is safe (and optimal) to pop it now.

✅ Why?
Because:

* If you delay popping this small char, you **risk putting bigger characters on top** and making `res` lexicographically worse.
* You can **safely pop** all characters from the stack that are **no worse than** what remains in `s`.

---

## 📦 Example Walkthrough: `"bac"`

| Step | char | cnt      | stack | minChar | condition to pop (`stack[-1] <= minChar`) | res |
| ---- | ---- | -------- | ----- | ------- | ----------------------------------------- | --- |
| 1    | b    | a:1, c:1 | b     | a       | ❌ 'b' > 'a'                               |     |
| 2    | a    | c:1      | b a   | a       | ✅ pop 'a'                                 | a   |
|      |      |          | b     | a       | ✅ pop 'b'                                 | ab  |
| 3    | c    | (empty)  | c     | z       | ✅ pop 'c'                                 | abc |

Final result: `"abc"`

---

## 🧠 Why This Works

This solution is **functionally equivalent** to the `min_suffix[]` idea, but instead of precomputing suffix mins, it:

* Tracks character availability using a `Counter`
* Dynamically adjusts the smallest "still-to-come" character with `minCharacter`

It’s **greedy**, space-efficient (no suffix array), and elegant.

---

## ✅ Summary

| Concept                     | Why it’s used                                          |
| --------------------------- | ------------------------------------------------------ |
| `Counter(s)`                | Know what characters are still available in future `s` |
| `minCharacter`              | Track smallest remaining char (like `min_suffix[i]`)   |
| `stack`                     | Simulate robot’s held characters                       |
| `stack[-1] <= minCharacter` | Safe condition to pop from `t`                         |
| `res.append(...)`           | Build lexicographically smallest result                |

---

Would you like to try tracing it on a trickier input like `"bdda"` and I’ll help walk you through it?

'''


'''
Awesome! Let’s walk through the input `s = "bdda"` step-by-step using your code logic, simulating exactly what happens in the **stack**, the **res**, the **Counter**, and how **`minCharacter`** evolves.

---

### 📦 Initial Setup:

```python
s = "bdda"
cnt = {'b': 1, 'd': 2, 'a': 1}
stack = []
res = []
minCharacter = 'a'
```

---

### 🔁 Step-by-Step Execution

#### 🔹 Step 1: char = `'b'`

```python
stack.append('b')  → stack = ['b']
cnt['b'] -= 1      → cnt = {'b': 0, 'd': 2, 'a': 1}
```

Now update `minCharacter`:

```python
while cnt['a'] != 0 → keep minCharacter = 'a'
```

Now check:

```python
stack[-1] = 'b'  > minCharacter 'a' → ❌ can't pop
```

➡️ **res = \[]**, **stack = \['b']**

---

#### 🔹 Step 2: char = `'d'`

```python
stack.append('d')  → stack = ['b', 'd']
cnt['d'] -= 1      → cnt = {'b': 0, 'd': 1, 'a': 1}
```

`minCharacter` is still `'a'` → (since `cnt['a'] == 1`)

```python
stack[-1] = 'd' > 'a' → ❌ no pop
```

➡️ **res = \[]**, **stack = \['b', 'd']**

---

#### 🔹 Step 3: char = `'d'`

```python
stack.append('d')  → stack = ['b', 'd', 'd']
cnt['d'] -= 1      → cnt = {'b': 0, 'd': 0, 'a': 1}
```

`minCharacter` still `'a'` (still left)

```python
stack[-1] = 'd' > 'a' → ❌ no pop
```

➡️ **res = \[]**, **stack = \['b', 'd', 'd']**

---

#### 🔹 Step 4: char = `'a'`

```python
stack.append('a')  → stack = ['b', 'd', 'd', 'a']
cnt['a'] -= 1      → cnt = {'b': 0, 'd': 0, 'a': 0}
```

Now update `minCharacter`:

```python
cnt['a'] == 0 → bump to 'b'
cnt['b'] == 0 → bump to 'c'
cnt['c'] == 0 → ...
→ Eventually: minCharacter becomes 'z'
```

Now pop while `stack[-1] <= minCharacter` (which is `'z'`)

```python
stack[-1] = 'a' → ✅ pop → res = ['a']
stack[-1] = 'd' → ✅ pop → res = ['a', 'd']
stack[-1] = 'd' → ✅ pop → res = ['a', 'd', 'd']
stack[-1] = 'b' → ✅ pop → res = ['a', 'd', 'd', 'b']
```

Now `stack` is empty.

---

### ✅ Final Result:

```python
res = ['a', 'd', 'd', 'b']
return ''.join(res) → "addb"
```

---

## ✅ Confirmed: Output = `"addb"` ✔

---

### 🧠 Key Takeaways from This Example:

| Step                                | Insight                                                         |
| ----------------------------------- | --------------------------------------------------------------- |
| Push one char at a time             | Simulates feeding robot one char from left to right             |
| `minCharacter` tracks what's safest | Ensures we don’t pop something that blocks a smaller char later |
| All chars get popped eventually     | Only timing of pop matters — greedy choice is key               |

Would you like to try stepping through a more complex input next (like `"zzaaz"`), or try rewriting this in your own words to test your understanding?

'''
