def subset(arr):

    n = len(arr)
    All_sets = []

    def dfs(index, path):

        if index == n:
            All_sets.append(path)
            return

        # Include the current element
        dfs(index + 1, path + [arr[index]])

        # Exclude the current element
        dfs(index + 1, path)

    dfs(0, [])
    return All_sets


print(subset([1, 2, 3]))
