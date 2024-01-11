'''
146. LRU Cache
Medium
Topics
Companies
Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:

LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
int get(int key) Return the value of the key if the key exists, otherwise return -1.
void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
The functions get and put must each run in O(1) average time complexity.

 

Example 1:

Input
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, null, -1, 3, 4]

Explanation
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // cache is {1=1}
lRUCache.put(2, 2); // cache is {1=1, 2=2}
lRUCache.get(1);    // return 1
lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.get(2);    // returns -1 (not found)
lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.get(1);    // return -1 (not found)
lRUCache.get(3);    // return 3
lRUCache.get(4);    // return 4
 

Constraints:

1 <= capacity <= 3000
0 <= key <= 104
0 <= value <= 105
At most 2 * 105 calls will be made to get and put.
'''


class LRUCache:
    def __init__(self, capacity: int):
        print(f"Initializing an LRU Cache with capacity {capacity}")
        self.cache = {}
        self.freeSpace = capacity

    def get(self, key: int) -> int:
        print(f"Getting the value for key {key}")
        if key not in self.cache:
            print(f"Key {key} not found in the cache")
            return -1

        # Move the key to the end to mark it as recently used
        self.cache[key] = self.cache.pop(key)
        print(f"Key {key} found in the cache with value {self.cache[key]}")
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        print(f"Putting key-value pair {key}-{value} into the cache")
        if key in self.cache:
            print(f"Key {key} already exists in the cache, updating its value")
            self.cache.pop(key)
        else:
            if self.freeSpace:
                print(f"There is free space in the cache")
                self.freeSpace -= 1
            else:
                # Remove the least recently used item
                least_recently_used_key = next(iter(self.cache))
                print(f"No free space in the cache, evicting the least recently used key {
                      least_recently_used_key}")
                self.cache.pop(least_recently_used_key)

        # Add the new key-value pair to the cache
        self.cache[key] = value
        print(f"Key-value pair {key}-{value} is put into the cache")


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
