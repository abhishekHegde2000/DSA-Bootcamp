'''
B. Painting Eggs
time limit per test5 seconds
memory limit per test256 megabytes
The Bitlandians are quite weird people. They have very peculiar customs.

As is customary, Uncle J. wants to have n eggs painted for Bitruz (an ancient Bitland festival). He has asked G. and A. to do the work.

The kids are excited because just as is customary, they're going to be paid for the job!

Overall uncle J. has got n eggs. G. named his price for painting each egg. Similarly, A. named his price for painting each egg. It turns out that for each egg the sum of the money both A. and G. want for the painting equals 1000.

Uncle J. wants to distribute the eggs between the children so as to give each egg to exactly one child. Also, Uncle J. wants the total money paid to A. to be different from the total money paid to G. by no more than 500.

Help Uncle J. Find the required distribution of eggs or otherwise say that distributing the eggs in the required manner is impossible.

Input
The first line contains integer n (1 ≤ n ≤ 106) — the number of eggs.

Next n lines contain two integers ai and gi each (0 ≤ ai, gi ≤ 1000; ai + gi = 1000): ai is the price said by A. for the i-th egg and gi is the price said by G. for the i-th egg.

Output
If it is impossible to assign the painting, print "-1" (without quotes).

Otherwise print a string, consisting of n letters "G" and "A". The i-th letter of this string should represent the child who will get the i-th egg in the required distribution. Letter "A" represents A. and letter "G" represents G. If we denote the money Uncle J. must pay A. for the painting as Sa, and the money Uncle J. must pay G. for the painting as Sg, then this inequality must hold: |Sa  -  Sg|  ≤  500.

If there are several solutions, you are allowed to print any of them.

Examples
InputCopy
2
1 999
999 1
OutputCopy
AG
InputCopy
3
400 600
400 600
400 600
OutputCopy
AGA

'''


def assign_eggs(n, costs):
    Sa = 0  # Total cost paid to A
    Sg = 0  # Total cost paid to G
    result = []  # Assignment string

    for i in range(n):
        a_i, g_i = costs[i]

        # Check if assigning to A keeps |Sa - Sg| <= 500
        if abs((Sa + a_i) - Sg) <= 500:
            Sa += a_i
            result.append("A")
        elif abs(Sa - (Sg + g_i)) <= 500:
            Sg += g_i
            result.append("G")
        else:
            return "-1"  # Not possible to assign eggs

    return "".join(result)


# Input reading and execution
if __name__ == "__main__":
    n = int(input().strip())  # Number of eggs
    costs = [tuple(map(int, input().split())) for _ in range(n)]
    print(assign_eggs(n, costs))
