
# Sources : Algorithms and Data Structures in Python (by Holczer Balazs on Udemy)

# Integer reversion problem

# Our task is to design an efficient algorithm to reverse a given integer.
# For example if the input of the algorithm is 1234 then the output should be 4321.

from ReverseArray import reverse

def reverse_integer(num):

    reversed = 0

    while num > 0:
        # extract last digit
        remainder = num % 10
        # push last digit to reversed
        reversed = reversed * 10 + remainder
        # abandon last digit
        num = num // 10

    return reversed

if __name__ == '__main__':
    
    num1 = 12345678
    num2 = 2030
    print(reverse_integer(num1))
    # comparing with reverse function previously defined
    print(int(''.join(reverse(list(str(num1))))))

    # test the case that has 0 in last digit
    print(reverse_integer(num2))
    print(int(''.join(reverse(list(str(num2))))))