import sys
sys.stdout.reconfigure(encoding='utf-8')

# test here


from typing import List

class Visualizer:
    """
    Handles the 'Debugger View' of the algorithm.
    Responsible strictly for formatting and printing state snapshots.
    """
    @staticmethod
    def print_snapshot(step_name: str, commentary: str, memory_state: dict):
        print(f"\n{'='*60}")
        print(f"SNAPSHOT: {step_name}")
        print(f"LOGIC   : {commentary}")
        print(f"{'-'*60}")
        print("MEMORY STATE:")
        for var_name, value in memory_state.items():
            # Format lists/dicts for cleaner reading if they are long
            val_str = str(value)
            print(f"   ► {var_name:<28} : {val_str}")
        print(f"{'='*60}\n")

class Solution:
    def countTrapezoids(self, input_points: List[List[int]]) -> int:
        """
        Calculates horizontal trapezoids with a visualized execution flow.
        """
        MOD = 10**9 + 7
        viz = Visualizer()
        
        # --- PHASE 1: PRE-PROCESSING ---
        # Group points by Y-coordinate (Row Level).
        # We use a hash map because we need to know "How many points are on this line?"
        points_per_y_level = {}
        for _, y_coord in input_points:
            points_per_y_level[y_coord] = points_per_y_level.get(y_coord, 0) + 1
            
        viz.print_snapshot(
            "Grouping Points",
            "Mapped all points to their Y-levels. Keys=Y-coord, Values=Count.",
            {"input_points": input_points, "points_per_y_level": points_per_y_level}
        )

        total_trapezoids = 0
        
        # This variable represents the sum of ALL valid segments (bases) found in ALL previous rows.
        accumulated_history_segments = 0
        
        # --- PHASE 2: ITERATION ---
        # Iterate through the counts. The specific Y-value doesn't matter, 
        # only the number of points at that level matters.
        sorted_levels = sorted(points_per_y_level.items()) # Sorting just for cleaner visual output order
        
        for y_coord, point_count in sorted_levels:
            
            # Constraint: A line needs at least 2 points to form a base.
            if point_count < 2:
                viz.print_snapshot(
                    f"Skipping Level Y={y_coord}",
                    f"Found {point_count} point(s). Need >= 2 to form a segment.",
                    {"current_y": y_coord, "point_count": point_count}
                )
                continue

            # Step A: Calculate valid segments on THIS row.
            # Formula: n * (n - 1) / 2
            current_level_segments = (point_count * (point_count - 1)) // 2
            
            # Step B: Connect THIS row to HISTORY.
            # Distributive property: Current Segments * Sum of All Previous Segments
            new_trapezoids_found = (current_level_segments * accumulated_history_segments)
            
            # Update Total
            previous_total = total_trapezoids
            total_trapezoids = (total_trapezoids + new_trapezoids_found) % MOD
            
            viz.print_snapshot(
                f"Processing Level Y={y_coord}",
                "Pairing current segments with history. Updating total.",
                {
                    "current_y": y_coord,
                    "point_count": point_count,
                    "current_level_segments": f"{current_level_segments} (calculated via nC2)",
                    "accumulated_history": accumulated_history_segments,
                    "calculation": f"{current_level_segments} * {accumulated_history_segments} = {new_trapezoids_found} new shapes",
                    "total_trapezoids": f"{previous_total} -> {total_trapezoids}"
                }
            )
            
            # Step C: Update History for the NEXT row.
            accumulated_history_segments = (accumulated_history_segments + current_level_segments) % MOD

        # --- PHASE 3: RESULT ---
        viz.print_snapshot(
            "Final Result",
            "Algorithm complete. Returning accumulated count.",
            {"Final Answer": total_trapezoids}
        )
        
        return total_trapezoids

# ==========================================
# TEST EXECUTION LAB
# ==========================================
solver = Solution()

print("\n\n>>> TEST CASE 1: Standard Trapezoid Scenario")
# Matches the example: Row Y=0 has 3 points, Row Y=2 has 2 points.
points_1 = [[1,0], [2,0], [3,0], [2,2], [3,2]]
solver.countTrapezoids(points_1)

print("\n\n>>> TEST CASE 2: Multi-Layer Scenario (Accumulation Logic)")
# Row Y=0 (3 pts), Row Y=1 (2 pts), Row Y=2 (2 pts)
# This tests if Row 2 connects to BOTH Row 0 and Row 1 correctly.
points_2 = [
    [0,0], [1,0], [2,0], # 3 points (3 segments)
    [0,1], [1,1],        # 2 points (1 segment)
    [0,2], [2,2]         # 2 points (1 segment)
]
solver.countTrapezoids(points_2)