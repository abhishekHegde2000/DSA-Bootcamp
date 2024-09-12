# different ways take 2 inputs and substract 2 binary numbers
from adding_two_numbers import take_input

'''
input example:

N = 3  - number of testcases

5 3 - 101 11

4 12 - 100 1100

5 5 - 101 101

'''


testcases = take_input()


def sub_binary_numbers(testcases):
    for testcase in testcases:
        num1 = testcase[0]
        num2 = testcase[1]
        borrow = 0
        result = 0
        i = 0
        while num1 > 0 or num2 > 0:
            # get the rightmost bit of num1
            bit1 = num1 & 1
            # get the rightmost bit of num2
            bit2 = num2 & 1
            # subtract the bits along with the borrow
            diff = bit1 - bit2 - borrow
            # update the borrow
            borrow = 0
            if diff < 0:
                diff += 2
                borrow = 1
            # update the result
            result |= diff << i
            # right shift both numbers
            num1 >>= 1
            num2 >>= 1
            i += 1
        print(result)


def sub_binary_numbers_using_decimals(testcases):
    for testcase in testcases:
        num1 = testcase[0]
        num2 = testcase[1]
        print(bin(num1 - num2)[2:])
        

def binary_subtraction(num1, num2):
    # Convert binary strings to integers
    dec_num1 = int(num1, 2)
    dec_num2 = int(num2, 2)
    
    # Subtract the numbers
    result = dec_num1 - dec_num2
    
    # Convert result back to binary and remove '0b' prefix
    binary_result = bin(result)[2:]
    
    return binary_result