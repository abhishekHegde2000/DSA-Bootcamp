'''
Implement the RandomizedSet class:

RandomizedSet() Initializes the RandomizedSet object.
bool insert(int val) Inserts an item val into the set if not present. Returns true if the item was not present, false otherwise.
bool remove(int val) Removes an item val from the set if present. Returns true if the item was present, false otherwise.
int getRandom() Returns a random element from the current set of elements (it's guaranteed that at least one element exists when this method is called). Each element must have the same probability of being returned.
You must implement the functions of the class such that each function works in average O(1) time complexity.

 

Example 1:

Input
["RandomizedSet", "insert", "remove", "insert", "getRandom", "remove", "insert", "getRandom"]
[[], [1], [2], [2], [], [1], [2], []]
Output
[null, true, false, true, 2, true, false, 2]

Explanation
RandomizedSet randomizedSet = new RandomizedSet();
randomizedSet.insert(1); // Inserts 1 to the set. Returns true as 1 was inserted successfully.
randomizedSet.remove(2); // Returns false as 2 does not exist in the set.
randomizedSet.insert(2); // Inserts 2 to the set, returns true. Set now contains [1,2].
randomizedSet.getRandom(); // getRandom() should return either 1 or 2 randomly.
randomizedSet.remove(1); // Removes 1 from the set, returns true. Set now contains [2].
randomizedSet.insert(2); // 2 was already in the set, so return false.
randomizedSet.getRandom(); // Since 2 is the only number in the set, getRandom() will always return 2.

'''

from typing import List

import random


class RandomizedSet:
    def __init__(self):
        # Initialize a dictionary to store the values and their indices
        self.val_to_index = {}
        # Initialize a list to store the values
        self.values = []

    def insert(self, val: int) -> bool:
        # Check if the value is not in the dictionary
        not_present = val not in self.val_to_index
        if not_present:
            # Add the value to the dictionary and list
            self.val_to_index[val] = len(self.values)
            self.values.append(val)
        return not_present

    def remove(self, val: int) -> bool:
        # Check if the value is in the dictionary
        present = val in self.val_to_index
        if present:
            # Get the index of the value
            index = self.val_to_index[val]
            # Get the last value in the list
            last_val = self.values[-1]
            # Replace the value to be removed with the last value
            self.values[index] = last_val
            # Remove the last value from the list
            self.values.pop()
            # Update the index of the last value
            self.val_to_index[last_val] = index
            # Remove the value from the dictionary
            del self.val_to_index[val]
        return present

    def getRandom(self) -> int:
        # Return a random value from the list
        return random.choice(self.values)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
