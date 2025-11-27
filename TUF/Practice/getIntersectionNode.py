import sys
sys.stdout.reconfigure(encoding='utf-8')

# test here


import time

# ==========================================
# DATA STRUCTURES
# ==========================================

class ListNode:
    def __init__(self, value):
        self.val = value
        self.next = None
    
    def __repr__(self):
        return f"Node({self.val})"

# ==========================================
# VISUALIZATION ENGINE
# ==========================================

class Visualizer:
    def __init__(self):
        self.step_counter = 1

    def print_snapshot(self, message, pointer_a, pointer_b, head_a, head_b):
        """
        Renders the current state of both lists and the positions of pointers A and B.
        """
        print(f"\n{'-'*60}")
        print(f"SNAPSHOT #{self.step_counter}: {message}")
        print(f"{'-'*60}")
        
        # Visualize List A state
        print("List A Structure:")
        self._render_list_with_pointers(head_a, pointer_a, pointer_b, "A")
        
        # Visualize List B state
        print("\nList B Structure:")
        self._render_list_with_pointers(head_b, pointer_a, pointer_b, "B")
        
        # Print Pointer States
        val_a = f"[{pointer_a.val}]" if pointer_a else "None (Switching)"
        val_b = f"[{pointer_b.val}]" if pointer_b else "None (Switching)"
        
        print(f"\n> Pointer A is at: {val_a}")
        print(f"> Pointer B is at: {val_b}")
        
        # Check for intersection match visually
        if pointer_a and pointer_b and pointer_a is pointer_b:
            print(f"\n*** MATCH FOUND AT ADDRESS {id(pointer_a)} ***")
        
        self.step_counter += 1
        # Small delay for dramatic effect if running in a real console
        # time.sleep(0.5) 

    def _render_list_with_pointers(self, head, ptr_a, ptr_b, list_name):
        """
        Helper to draw the list as [Box] -> [Box] with arrows underneath pointing to current nodes.
        """
        current = head
        nodes_line = ""
        arrows_line = ""
        
        while current:
            # Create Node Box
            node_str = f"[{current.val}]"
            nodes_line += node_str + " --> "
            
            # Calculate spacing for the arrow line
            # We need to center the arrow under the box
            padding = len(node_str)
            marker = ""
            
            # Check if pointers are here
            is_a = (current is ptr_a)
            is_b = (current is ptr_b)
            
            if is_a and is_b:
                marker = "^A&B"
            elif is_a:
                marker = "^PtrA"
            elif is_b:
                marker = "^PtrB"
            else:
                marker = " " * padding # Empty space
            
            # Center the marker relative to the node box width
            # Box is roughly 3-5 chars. 
            # If marker is longer (e.g. ^PtrA), we might need logic, but simplified:
            # Just align left for now to keep code simple without external libs.
            
            # Formatting alignment
            spaces_needed = len(node_str) - len(marker)
            if spaces_needed > 0:
                marker += " " * spaces_needed
            else:
                # If marker is wider than box (rare with these short names), just let it be
                pass
            
            arrows_line += marker + "     " # 5 spaces for ' --> '
            
            current = current.next
            
        nodes_line += "None"
        print(f"  {nodes_line}")
        print(f"  {arrows_line}")

# ==========================================
# ALGORITHM IMPLEMENTATION
# ==========================================

class Solution:
    def getIntersectionNode(self, head_a: ListNode, head_b: ListNode) -> ListNode:
        viz = Visualizer()
        
        pointer_a = head_a
        pointer_b = head_b
        
        viz.print_snapshot("Initialization: Pointers start at heads.", pointer_a, pointer_b, head_a, head_b)

        while pointer_a != pointer_b:
            # Logic: Move forward. If None, switch tracks.
            
            # --- Move Pointer A ---
            if pointer_a is None:
                pointer_a = head_b
                comment_a = "Pointer A hit End -> Jumps to Head B"
            else:
                pointer_a = pointer_a.next
                comment_a = "Pointer A moves next"

            # --- Move Pointer B ---
            if pointer_b is None:
                pointer_b = head_a
                comment_b = "Pointer B hit End -> Jumps to Head A"
            else:
                pointer_b = pointer_b.next
                comment_b = "Pointer B moves next"

            # Generate Comment
            if pointer_a == pointer_b and pointer_a is not None:
                status = "INTERSECTION FOUND!"
            elif pointer_a is None and pointer_b is None:
                status = "End of both lists reached (No Intersection)."
            elif pointer_a is None or pointer_b is None:
                 status = "One pointer is switching tracks..."
            else:
                status = "Advancing..."

            viz.print_snapshot(status, pointer_a, pointer_b, head_a, head_b)
        
        return pointer_a

# ==========================================
# TEST SCENARIO
# ==========================================

print("=== VISUAL EXECUTION LAB: INTERSECTION OF LINKED LISTS ===")

# Constructing the Intersection Scenario (Y-Shape)
# List A: 4 -> 1 -> 8 -> 4 -> 5
# List B: 5 -> 6 -> 1 -> 8 -> 4 -> 5
# Intersection at Node(8)

# Shared Part
common = ListNode(8)
common.next = ListNode(4)
common.next.next = ListNode(5)

# List A distinctive part
head_a = ListNode(4)
head_a.next = ListNode(1)
head_a.next.next = common  # Connect to shared

# List B distinctive part
head_b = ListNode(5)
head_b.next = ListNode(6)
head_b.next.next = ListNode(1)
head_b.next.next.next = common # Connect to shared

# Run Logic
sol = Solution()
result = sol.getIntersectionNode(head_a, head_b)

print(f"\nFinal Result: {result}")