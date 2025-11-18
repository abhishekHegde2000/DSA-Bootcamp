from bisect import bisect_right

def findMedianSortedMatrix(matrix):
    """
    Finds the median of a row-wise sorted matrix using Binary Search on Value.
    """

    # --- 1. SETUP & INPUT ANALYSIS ---
    rowCount = len(matrix)
    colCount = len(matrix[0])
    totalElements = rowCount * colCount

    # The median is the element at this rank (1-based count) in a sorted list.
    # Example: 9 elements. Median is the 5th smallest. (9//2 + 1 = 5)
    targetMedianRank = totalElements // 2 + 1

    print(f"\n{'='*60}")
    print(f"🛠️  INITIALIZING ALGORITHM")
    print(f"{'='*60}")
    print(f"📥 Input Matrix Size : {rowCount} rows x {colCount} columns")
    print(f"🔢 Total Elements    : {totalElements}")
    print(f"🎯 Target Median Rank: {targetMedianRank} (We need the {targetMedianRank}-th smallest number)")

    # Calculate the Search Space (Range of possible answers)
    # The median cannot be smaller than the smallest element in the grid
    # nor larger than the largest element.
    searchSpaceLow = float('inf')
    searchSpaceHigh = float('-inf')

    for rowIndex in range(rowCount):
        # Row is sorted, so min is at index 0, max is at last index
        searchSpaceLow = min(searchSpaceLow, matrix[rowIndex][0])
        searchSpaceHigh = max(searchSpaceHigh, matrix[rowIndex][colCount - 1])

    print(f"🔍 Search Space Defined: [{searchSpaceLow}, {searchSpaceHigh}]")
    print(f"   Why? The median must physically exist within this value range.")
    print(f"{'-'*60}")

    step = 0

    # --- 2. BINARY SEARCH LOOP ---
    while searchSpaceLow <= searchSpaceHigh:
        step += 1

        # Pick a number in the middle of our current value range
        guessedMedian = (searchSpaceLow + searchSpaceHigh) // 2

        print(f"\n[Step {step}] Binary Search Iteration")
        print(f"   Current Range : [{searchSpaceLow}, {searchSpaceHigh}]")
        print(f"   Guessed Value : {guessedMedian}")
        print(f"   ❓ Question   : Are there at least {targetMedianRank} numbers <= {guessedMedian}?")

        # --- 3. COUNTING ELEMENTS (The Logic Check) ---
        countSmallerOrEqual = 0

        # We iterate through every row to count how many numbers are <= guessedMedian.
        # Since rows are sorted, we use bisect_right (upper bound) for speed.
        for r in range(rowCount):
            # bisect_right returns the insertion point, which equals the number of elements <= guess
            countInRow = bisect_right(matrix[r], guessedMedian)
            countSmallerOrEqual += countInRow

            # Optional detailed log for the first few steps to see the math
            if step <= 2:
                print(f"      Row {r} {matrix[r]}: Found {countInRow} elements <= {guessedMedian}")

        print(f"   👉 Total Count: {countSmallerOrEqual}")

        # --- 4. CONDITIONAL UPDATES ---
        if countSmallerOrEqual < targetMedianRank:
            # CASE: We don't have enough numbers.
            # The guessedMedian is too small to be the median.
            print(f"   ❌ Condition: {countSmallerOrEqual} < {targetMedianRank} (Too Small)")
            print(f"   🧠 Logic    : We need more numbers to reach rank {targetMedianRank}.")
            print(f"                 So, the actual median must be > {guessedMedian}.")

            oldLow = searchSpaceLow
            searchSpaceLow = guessedMedian + 1
            print(f"   🔄 Update   : Moving Lower Bound: {oldLow} -> {searchSpaceLow}")

        else:
            # CASE: We have enough (or too many) numbers.
            # guessedMedian is a valid candidate, BUT we want the exact median.
            # We try to squeeze the range to the left to see if a smaller number also works.
            print(f"   ✅ Condition: {countSmallerOrEqual} >= {targetMedianRank} (Candidate Found)")
            print(f"   🧠 Logic    : {guessedMedian} might be the median, or a number smaller than it.")
            print(f"                 We eliminate numbers > {guessedMedian} to find the *first* valid number.")

            oldHigh = searchSpaceHigh
            searchSpaceHigh = guessedMedian - 1
            print(f"   🔄 Update   : Moving Upper Bound: {oldHigh} -> {searchSpaceHigh}")

    # --- 5. FINAL RESULT ---
    print(f"\n{'='*60}")
    print(f"🎉 FINAL RESULT")
    print(f"{'='*60}")
    print(f"The loop ended because Low ({searchSpaceLow}) > High ({searchSpaceHigh}).")
    print(f"The smallest value that satisfied the rank condition is stored in Low.")
    print(f"👉 Median = {searchSpaceLow}")
    return searchSpaceLow

# --- TEST CASES ---

print("\n\n🔵 --- TEST CASE 1 ---")
matrix1 = [
    [1, 4, 9],
    [2, 5, 6],
    [3, 7, 8]
]
findMedianSortedMatrix(matrix1)


print("\n\n🔵 --- TEST CASE 2 (Overlapping Values) ---")
matrix2 = [
    [1, 3, 8],
    [2, 3, 4],
    [1, 2, 5]
]
findMedianSortedMatrix(matrix2)
