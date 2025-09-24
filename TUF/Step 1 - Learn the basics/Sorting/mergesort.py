class Solution:
    def mergeSort(self, nums):
        n = len(nums)

        # Base case
        if n <= 1:
            return nums

        # Find mid
        mid = n // 2

        # Split into left and right halves
        leftArray = nums[:mid]
        rightArray = nums[mid:]

        # Recursively sort both halves
        sortedLeft = self.mergeSort(leftArray)
        sortedRight = self.mergeSort(rightArray)

        # Merge the two sorted halves
        return self.merge(sortedLeft, sortedRight)

    def merge(self, left, right):
        result = []
        i = j = 0

        # Merge two sorted arrays
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

        # Add remaining elements
        result.extend(left[i:])
        result.extend(right[j:])

        return result


# Example usage
sol = Solution()
print(sol.mergeSort([5, 2, 9, 1, 3, 6]))
