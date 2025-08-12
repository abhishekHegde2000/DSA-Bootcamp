class Solution:
    def quickSort(self, nums):
        def partition(arr, low, high):
            pivot = arr[high]  # pick last element as pivot
            i = low - 1

            for j in range(low, high):
                print(f"Compare {arr[j]} with pivot {pivot}")
                if arr[j] <= pivot:
                    i += 1
                    arr[i], arr[j] = arr[j], arr[i]
                    print(f"  Swapped -> {arr}")

            arr[i + 1], arr[high] = arr[high], arr[i + 1]
            print(f"Placed pivot {pivot} at index {i+1} -> {arr}")
            return i + 1

        def quick_sort_recursive(arr, low, high):
            if low < high:
                pi = partition(arr, low, high)
                print(f"Pivot {arr[pi]} is fixed at index {pi}\n")

                # Sort left and right subarrays
                print(f"Left part: {arr[low:pi]}")
                quick_sort_recursive(arr, low, pi - 1)

                print(f"Right part: {arr[pi+1:high+1]}")
                quick_sort_recursive(arr, pi + 1, high)

        quick_sort_recursive(nums, 0, len(nums) - 1)
        return nums


arr = [10, 7, 8, 9, 1, 5]
sol = Solution()
sorted_arr = sol.quickSort(arr)
print("Final sorted array:", sorted_arr)
