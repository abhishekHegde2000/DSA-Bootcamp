'''
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:

Input: strs = [""]
Output: [[""]]
Example 3:

Input: strs = ["a"]
Output: [["a"]]
'''

from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Initialize an empty hashmap
        anagram_groups = {}

        # Iterate over the list of strings
        for string in strs:
            print(f"Processing string: {string}")

            # Count the number of occurrences of each character
            char_count = [0] * 26
            for char in string:
                char_count[ord(char) - ord('a')] += 1
            key = tuple(char_count)
            print(f"Key for string: {key}")

            # If the key is not in the hashmap, add the string to the hashmap with the key
            if key not in anagram_groups:
                anagram_groups[key] = [string]
                print(f"Added new group with string: {string}")
            # If the key is in the hashmap, append the string to the list of strings that have the same key
            else:
                anagram_groups[key].append(string)
                print(f"Added string to existing group: {string}")

        # Return the list of strings for each key in the hashmap
        return list(anagram_groups.values())


sol = Solution()
print(sol.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
print(sol.groupAnagrams([""]))
print(sol.groupAnagrams(["a"]))


'''

Python 3 || brute force -> optimized || sorting || Hashmap

# Intuition
The problem is asking to group anagrams together. An anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once. A simple way to solve this problem is by using a hashmap. We can iterate over the list and for each string, we count the number of occurrences of each character and use this as a key in a hashmap. All strings that are anagrams will have the same key.

# Approach
1. Initialize an empty hashmap.
2. Iterate over the list of strings.
3. For each string, count the number of occurrences of each character and use this as a key in the hashmap.
4. If the key is not in the hashmap, add the string to the hashmap with the key.
5. If the key is in the hashmap, append the string to the list of strings that have the same key.
6. Return the list of strings for each key in the hashmap.

# Pseudo Code
```
Initialize an empty hashmap
For each string in the list
    Count the number of occurrences of each character and use this as a key
    If the key is not in the hashmap
        Add the string to the hashmap with the key
    If the key is in the hashmap
        Append the string to the list of strings that have the same key
Return the list of strings for each key in the hashmap
```

# Complexity
- Time complexity: O(n * m) - We are iterating over the list once and for each string, we are counting the number of occurrences of each character.
- Space complexity: O(n * m) - We are creating a hashmap to store the strings and their keys.

```python []
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Initialize an empty hashmap
        anagram_groups = {}
        
        # Iterate over the list of strings
        for string in strs:
            print(f"Processing string: {string}")
            
            # Count the number of occurrences of each character
            char_count = [0] * 26
            for char in string:
                char_count[ord(char) - ord('a')] += 1
            key = tuple(char_count)
            print(f"Key for string: {key}")
            
            # If the key is not in the hashmap, add the string to the hashmap with the key
            if key not in anagram_groups:
                anagram_groups[key] = [string]
                print(f"Added new group with string: {string}")
            # If the key is in the hashmap, append the string to the list of strings that have the same key
            else:
                anagram_groups[key].append(string)
                print(f"Added string to existing group: {string}")
        
        # Return the list of strings for each key in the hashmap
        return list(anagram_groups.values())
```
```python []
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Initialize an empty hashmap to store the groups of anagrams
        anagram_map = {}
        
        # Iterate over the list of strings
        for s in strs:
            print(f"Processing string: {s}")
            
            # Sort the string and use it as a key
            sorted_s = "".join(sorted(s))
            print(f"Key for string: {sorted_s}")
            
            # If the key is not in the hashmap, add the string to the hashmap with the key
            if sorted_s not in anagram_map:
                anagram_map[sorted_s] = [s]
                print(f"Added new group with string: {s}")
            # If the key is in the hashmap, append the string to the list of strings that have the same key
            else:
                anagram_map[sorted_s].append(s)
                print(f"Added string to existing group: {s}")
        
        # Return the list of strings for each key in the hashmap
        return list(anagram_map.values())

```
```python []
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Function to check if two strings are anagrams
        def areAnagrams(s1: str, s2: str) -> bool:
            return sorted(s1) == sorted(s2)

        groups = []
        for string1 in strs:
            # Flag to check if string1 is already in a group
            inGroup = False
            for group in groups:
                # If string1 is an anagram of the first string in the group
                if areAnagrams(string1, group[0]):
                    group.append(string1)
                    inGroup = True
                    break
            # If string1 is not in any group, create a new group
            if not inGroup:
                groups.append([string1])
        return groups
```



'''
