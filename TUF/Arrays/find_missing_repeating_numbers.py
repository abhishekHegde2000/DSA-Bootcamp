# test here
import sys

def find_missing_repeating_numbers(input_array: list[int]) -> list[int]:
    """
    Finds the repeating and missing numbers using the XOR method.
    Refactored for educational clarity with bit-level visualization.
    """
    n = len(input_array)
    
    print("\n" + "="*60)
    print(f"[SETUP] Algorithm: XOR Bit Manipulation")
    print(f"   🧠 Intuition: We will exploit 'A ^ A = 0'. By XORing the input array")
    print(f"      against the perfect sequence [1..N], everything cancels out except")
    print(f"      the Repeating number (appears 3 times -> 1 time) and the")
    print(f"      Missing number (appears 1 time).")
    print(f"   📥 Input Array: {input_array}")
    print(f"   🔢 Expected Range: 1 to {n}")
    print("="*60 + "\n")

    # --- PHASE 1: THE GREAT COLLISION ---
    # We XOR everything together to find (Repeating ^ Missing)
    
    combined_xor_diff = 0
    print("[PHASE 1] Accumulating XOR (Input Array vs Sequence 1..N)")
    
    for index in range(n):
        array_val = input_array[index]
        sequence_val = index + 1
        
        # Visualizing the accumulation
        old_xor = combined_xor_diff
        combined_xor_diff = combined_xor_diff ^ array_val
        combined_xor_diff = combined_xor_diff ^ sequence_val
        
        print(f"   🔄 Step {index+1}/{n}:")
        print(f"      Current XOR: {old_xor:04b} ({old_xor})")
        print(f"      ^ Array Val: {array_val:04b} ({array_val})")
        print(f"      ^ Seq Val  : {sequence_val:04b} ({sequence_val})")
        print(f"      --------------------")
        print(f"      = New Result: {combined_xor_diff:04b} ({combined_xor_diff})")

    # At this point, combined_xor_diff represents (Repeating ^ Missing)
    print(f"\n   🏁 Phase 1 Result: {combined_xor_diff} (Binary: {combined_xor_diff:04b})")
    print(f"      (This value is the XOR of the Missing and Repeating numbers)")

    # --- PHASE 2: THE SEPARATOR ---
    # Find the rightmost set bit to distinguish the two numbers
    
    # Logic: A & -A isolates the rightmost 1-bit
    rightmost_set_bit = combined_xor_diff & -combined_xor_diff
    
    print("\n[PHASE 2] Finding the 'Differentiating Bit'")
    print(f"   ❓ Problem: We have X^Y, but we need X and Y separately.")
    print(f"   💡 Logic: Since X != Y, they must differ at some bit position.")
    print(f"      We pick the rightmost bit where they differ.")
    print(f"   ⚙️  Calculation: {combined_xor_diff} & -{combined_xor_diff}")
    print(f"   🎯 Resulting Mask: {rightmost_set_bit} (Binary: {rightmost_set_bit:04b})")
    print(f"      (We will use this bit to split all numbers into two 'buckets')")

    # --- PHASE 3: THE BUCKET SPLIT ---
    # Separate all numbers (array + sequence) into two buckets based on the bit
    
    bucket_unset_bit = 0 # Bucket for numbers where bit is 0
    bucket_set_bit = 0   # Bucket for numbers where bit is 1
    
    print("\n[PHASE 3] Grouping into Buckets")
    
    for index in range(n):
        # 1. Process Array Number
        arr_num = input_array[index]
        if (arr_num & rightmost_set_bit) != 0:
            bucket_set_bit ^= arr_num
            print(f"      Array Num {arr_num} -> Bucket SET (Bit is 1)")
        else:
            bucket_unset_bit ^= arr_num
            print(f"      Array Num {arr_num} -> Bucket UNSET (Bit is 0)")
            
        # 2. Process Sequence Number
        seq_num = index + 1
        if (seq_num & rightmost_set_bit) != 0:
            bucket_set_bit ^= seq_num
            print(f"      Seq Num   {seq_num} -> Bucket SET (Bit is 1)")
        else:
            bucket_unset_bit ^= seq_num
            print(f"      Seq Num   {seq_num} -> Bucket UNSET (Bit is 0)")

    print(f"   📦 Bucket UNSET Final XOR: {bucket_unset_bit}")
    print(f"   📦 Bucket SET Final XOR:   {bucket_set_bit}")
    print(f"   🔎 Inference: One of these is Repeating, the other is Missing.")

    # --- PHASE 4: IDENTIFICATION ---
    # Determine which candidate is the repeating one by checking the input array
    
    candidate_one = bucket_unset_bit
    candidate_two = bucket_set_bit
    
    print("\n[PHASE 4] Identifying Repeating vs Missing")
    print(f"   🕵️  Candidates: {candidate_one} and {candidate_two}")
    
    frequency_count = 0
    for num in input_array:
        if num == candidate_one:
            frequency_count += 1
            
    print(f"   📝 Check: Candidate {candidate_one} appears {frequency_count} times in input.")

    repeating_number = -1
    missing_number = -1

    if frequency_count == 2:
        print(f"   ✅ Conclusion: {candidate_one} is the REPEATING number.")
        repeating_number = candidate_one
        missing_number = candidate_two
    else:
        print(f"   ✅ Conclusion: {candidate_one} appears {frequency_count} times (expected 2 if repeating).")
        print(f"      Therefore, {candidate_two} must be REPEATING, and {candidate_one} is MISSING.")
        repeating_number = candidate_two
        missing_number = candidate_one

    print("\n" + "="*60)
    print(f"[RESULT] Repeating: {repeating_number}, Missing: {missing_number}")
    print(f"[ANALYSIS] Time: O(N) (Two passes) | Space: O(1) (No extra structures)")
    print("="*60 + "\n")
    
    return [repeating_number, missing_number]

# ---------------------------------------------------------
# TEST CASES
# ---------------------------------------------------------

# Test Case 1: Standard Example
# Array: [4, 3, 6, 2, 1, 1] (Size 6)
# Missing: 5, Repeating: 1
print(">>> TEST CASE 1: Standard Input")
find_missing_repeating_numbers([4, 3, 6, 2, 1, 1])

# Test Case 2: Swapped Position (Missing/Repeating swapped relative to bit logic)
# Array: [3, 1, 2, 5, 3] (Size 5)
# Range: 1, 2, 3, 4, 5
# Missing: 4, Repeating: 3
print(">>> TEST CASE 2: Repeating Number is 'Larger'")
find_missing_repeating_numbers([3, 1, 2, 5, 3])

# Test Case 3: Smallest Possible Input (Edge Case)
# Array: [2, 2] (Size 2)
# Range: 1, 2
# Missing: 1, Repeating: 2
print(">>> TEST CASE 3: Minimal Input Size")
find_missing_repeating_numbers([2, 2])