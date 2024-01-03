'''
We are given an array asteroids of integers representing asteroids in a row.

For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left). Each asteroid moves at the same speed.

Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.

 

Example 1:

Example 1:

Input: asteroids = [5,10,-5]
Output: [5,10]
Explanation: The 10 and -5 collide resulting in 10. The 5 and 10 never collide.
Example 2:

Input: asteroids = [8,-8]
Output: []
Explanation: The 8 and -8 collide exploding each other.
Example 3:

Input: asteroids = [10,2,-5]
Output: [10]
Explanation: The 2 and -5 collide resulting in -5. The 10 and -5 collide resulting in 10.

'''

from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        surviving_asteroids = []  # Initialize stack for surviving asteroids

        for current_asteroid in asteroids:
            print(f"Processing asteroid: {current_asteroid}")

            # Handle right-moving asteroids (push directly onto stack)
            if current_asteroid > 0:
                surviving_asteroids.append(current_asteroid)
                print(f"Pushed {current_asteroid} onto stack")

            # Handle collisions with left-moving asteroids
            elif current_asteroid < 0:
                while surviving_asteroids and surviving_asteroids[-1] > 0:
                    top_asteroid = surviving_asteroids[-1]
                    print(
                        f"Potential collision: {top_asteroid} vs {current_asteroid}")

                    if abs(top_asteroid) > abs(current_asteroid):  # Top asteroid wins
                        print(
                            f"Top asteroid {top_asteroid} wins, destroying {current_asteroid}")
                        current_asteroid = 0  # Destroy incoming asteroid
                        break  # No more collisions possible
                    elif abs(top_asteroid) < abs(current_asteroid):  # Incoming asteroid wins
                        print(
                            f"Incoming asteroid {current_asteroid} wins, destroying {top_asteroid}")
                        surviving_asteroids.pop()  # Destroy top asteroid
                    else:  # Both asteroids destroyed
                        print(
                            f"Both asteroids {top_asteroid} and {current_asteroid} destroyed")
                        surviving_asteroids.pop()  # Destroy top asteroid
                        current_asteroid = 0  # Destroy incoming asteroid
                        break  # No more collisions possible

                if current_asteroid:  # Push surviving left-moving asteroid onto stack
                    surviving_asteroids.append(current_asteroid)
                    print(f"Pushed {current_asteroid} onto stack")

        return surviving_asteroids


sol = Solution()
print(sol.asteroidCollision([5, 10, -5]))
print(sol.asteroidCollision([-2, 5, 10, -5]))
print(sol.asteroidCollision([-1, -10, -5]))
