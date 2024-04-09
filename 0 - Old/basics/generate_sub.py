def generate_subsequences(lst, index, current_sequence):
    # Base case: if the index is equal to the length of the list, print the current sequence
    if index == len(lst):
        print(current_sequence)
        return

    # Include the current element in the subsequence
    current_sequence.append(lst[index])
    generate_subsequences(lst, index + 1, current_sequence)
    current_sequence.pop()

    # Exclude the current element from the subsequence
    generate_subsequences(lst, index + 1, current_sequence)


def backtrack_subarrays(nums, start, path, result):
    result.append(path[:])

    for i in range(start, len(nums)):
        path.append(nums[i])
        backtrack_subarrays(nums, i + 1, path, result)
        path.pop()


def print_all_subarrays(nums):
    result = []
    backtrack_subarrays(nums, 0, [], result)
    return result


# Example usage:
nums = [1, 2, 3]
subarrays = print_all_subarrays(nums)

for subarray in subarrays:
    print(subarray)  # [1] [1, 2] [1, 2, 3] [1, 3] [2] [2, 3] [3]


# Example usage
my_list = [1, 2, 3]
# [1, 2, 3] [1, 2] [1, 3] [1] [2, 3] [2] [3] []
generate_subsequences(my_list, 0, [])


def backtrack_contiguous_subarrays(nums, start, path, result):
    if path:
        result.append(path[:])

    for i in range(start, len(nums)):
        path.append(nums[i])
        backtrack_contiguous_subarrays(nums, i + 1, path, result)
        path.pop()
