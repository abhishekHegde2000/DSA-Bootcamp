# different ways take 2 inputs and add 2 binary numbers

'''
input example:

N = 2  - number of testcases

4 12 - 100 1100 

5 5 - 101 101

'''


def take_input():
    N = int(input("enter the number of testcases: "))
    testcases = []
    for i in range(N):
        testcases.append(
            list(map(int, input("enter the values to add").split())))
    return testcases


def add_binary_numbers_with_bin(testcases):
    for testcase in testcases:
        print(bin(testcase[0] + testcase[1])[2:])

# can you create a functon to manually add 2 binary numbers?


def add_binary_numbers(testcases):
    for testcase in testcases:
        num1 = testcase[0]
        num2 = testcase[1]
        carry = 0
        result = 0
        i = 0
        while num1 > 0 or num2 > 0:
            # get the rightmost bit of num1
            bit1 = num1 & 1
            # get the rightmost bit of num2
            bit2 = num2 & 1
            # add the bits along with the carry
            sum = bit1 + bit2 + carry
            # update the carry
            carry = sum >> 1
            # update the result
            result |= (sum & 1) << i
            # right shift both numbers
            num1 >>= 1
            num2 >>= 1
            i += 1
        # if there is a carry left
        if carry:
            result |= carry << i
        print(result)


testcases = take_input()

add_binary_numbers(testcases)


'''

Let's break down the steps for num1 = 3 and num2 = 3:

Initial values:

num1 = 3 (binary: 11)
num2 = 3 (binary: 11)
carry = 0
result = 0
i = 0
First iteration:

bit1 = num1 & 1 -> bit1 = 1 (binary: 1)
bit2 = num2 & 1 -> bit2 = 1 (binary: 1)
sum = bit1 + bit2 + carry -> sum = 1 + 1 + 0 -> sum = 2 (binary: 10)
carry = sum >> 1 -> carry = 2 >> 1 -> carry = 1 (binary: 1)
result |= (sum & 1) << i -> result |= (2 & 1) << 0 -> result |= 0 -> result = 0 (binary: 0)
num1 >>= 1 -> num1 = 3 >> 1 -> num1 = 1 (binary: 1)
num2 >>= 1 -> num2 = 3 >> 1 -> num2 = 1 (binary: 1)
i += 1 -> i = 1
Second iteration:

bit1 = num1 & 1 -> bit1 = 1 (binary: 1)
bit2 = num2 & 1 -> bit2 = 1 (binary: 1)
sum = bit1 + bit2 + carry -> sum = 1 + 1 + 1 -> sum = 3 (binary: 11)
carry = sum >> 1 -> carry = 3 >> 1 -> carry = 1 (binary: 1)
result |= (sum & 1) << i -> result |= (3 & 1) << 1 -> result |= 1 << 1 -> result = 2 (binary: 10)
num1 >>= 1 -> num1 = 1 >> 1 -> num1 = 0 (binary: 0)
num2 >>= 1 -> num2 = 1 >> 1 -> num2 = 0 (binary: 0)
i += 1 -> i = 2
After the loop:

carry is 1, so result |= carry << i -> result |= 1 << 2 -> result = 6 (binary: 110)
Final result: 6 (binary: 110)

Running the provided code will print the intermediate values and the final result in binary format.
'''