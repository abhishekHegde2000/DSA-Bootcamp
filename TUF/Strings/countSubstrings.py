class Solution:
    def longestPalindrome(self, input_string: str) -> str:
        # ==============================================================================
        # HELPER: TERMINAL VISUALIZATION ENGINE
        # ==============================================================================
        def visualize_table(table, s, active_i=None, active_j=None):
            """
            Prints the DP table as a grid.
            - Uses '.' for False to reduce noise.
            - Uses 'T' for True.
            - Highlights the specific cell [active_i][active_j] being updated.
            """
            n = len(s)
            # Print Column Headers (Index + Char)
            headers = "      " + "   ".join(f"{idx}" for idx in range(n))
            chars   = "      " + "   ".join(f"{char}" for char in s)
            print(f"\n{headers}")
            print(f"{chars}")
            print("    " + "----" * n)

            for r in range(n):
                # Row Header (Index + Char)
                row_display = [f"{r} {s[r]} |"]
                for c in range(n):
                    val = table[r][c]
                    
                    # VISUAL LOGIC: formatting the cell
                    symbol = " T " if val else " . "
                    
                    # Highlight the active cell if provided
                    if r == active_i and c == active_j:
                        symbol = f"[{'T' if val else '.'}]" # e.g., [T]
                    
                    row_display.append(symbol)
                
                print(" ".join(row_display))
            print("\n")

        # ==============================================================================
        # PHASE 1: SETUP
        # ==============================================================================
        string_length = len(input_string)
        
        print(f"\n[SETUP] Analyzing String: '{input_string}'")
        print(f"[GOAL]  Fill the Table. 'T' means substring s[row:col+1] is a palindrome.")

        if string_length <= 1:
            return input_string

        # Initialize DP Table
        # is_palindrome_table[i][j] stores result for substring s[i...j]
        is_palindrome_table = [[False] * string_length for _ in range(string_length)]
        
        longest_palindrome_start = 0
        longest_palindrome_len = 1
        
        # ==============================================================================
        # PHASE 2: EXECUTION LOOP (Bottom-Up)
        # ==============================================================================
        # We iterate backwards (from last row up to 0) to ensure logic flow.
        
        for start_index in range(string_length - 1, -1, -1):
            
            for end_index in range(start_index, string_length):
                
                # LOGIC: Check boundaries
                match_boundaries = input_string[start_index] == input_string[end_index]
                
                # LOGIC: Check inner substring (Look 'down-left' in table)
                # If length is < 2 (single char or pair), we don't need inner check.
                # Otherwise, we rely on the pre-computed value at [start+1][end-1]
                
                if match_boundaries:
                    # Check if it's a small substring OR inner part is palindrome
                    if (end_index - start_index) < 2 or is_palindrome_table[start_index + 1][end_index - 1]:
                        
                        # 1. Update Truth Table
                        is_palindrome_table[start_index][end_index] = True
                        
                        # 2. Update Result if this is the new longest
                        current_len = end_index - start_index + 1
                        is_new_record = False
                        
                        if current_len > longest_palindrome_len:
                            longest_palindrome_start = start_index
                            longest_palindrome_len = current_len
                            is_new_record = True

                        # VISUALIZATION TRIGGER:
                        # We only print the full table when we find a TRUE palindrome 
                        # to show the "Evolution".
                        substring = input_string[start_index : end_index+1]
                        status = "🏆 NEW MAX!" if is_new_record else "✅ Palindrome Found"
                        
                        print(f"👉 Found '{substring}' at indices [{start_index}, {end_index}]. Status: {status}")
                        visualize_table(is_palindrome_table, input_string, start_index, end_index)

        # ==============================================================================
        # PHASE 3: FINAL RESULT
        # ==============================================================================
        result = input_string[longest_palindrome_start : longest_palindrome_start + longest_palindrome_len]
        print(f"[FINISHED] Final Longest Palindrome: '{result}'")
        return result

# ------------------------------------------------------------------------------
# TEST RUN
# ------------------------------------------------------------------------------
sol = Solution()
sol.longestPalindrome("babad")