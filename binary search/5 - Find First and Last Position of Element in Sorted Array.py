# Approach: Modified binary search to find first and last occurrences

# Pseudocode for search() method:
# 1. Initialize start and end pointers
# 2. While start <= end:
#   2.1 Calculate mid index
#   2.2 If target < mid, update end to mid-1 (search left)
#   2.3 If target > mid, update start to mid+1 (search right)
#   2.4 Else target == mid, update ans and move pointers based on startIndex
# 3. Return ans index

# Pseudocode for searchRange() method:
# 1. Initialize result array
# 2. Call search for first occurrence by passing startIndex=True
# 3. Call search for last occurrence by passing startIndex=False
# 4. Add first and last indices to result array
# 5. Return result array

class Solution:

    def search(self, nums, target, findFirst):

        left = 0
        right = len(nums) - 1
        result = -1

        while left <= right:

            mid = left + (right - left) // 2

            print(f"Searching nums[{left}:{right+1}]")

            if target < nums[mid]:
                right = mid - 1

            elif target > nums[mid]:
                left = mid + 1

            else:
                result = mid
                if findFirst:
                    right = mid - 1
                else:
                    left = mid + 1

        return result

    def searchRange(self, nums: List[int], target: int) -> List[int]:

        result = []

        first = self.search(nums, target, True)
        last = self.search(nums, target, False)

        result.append(first)
        result.append(last)

        return result
