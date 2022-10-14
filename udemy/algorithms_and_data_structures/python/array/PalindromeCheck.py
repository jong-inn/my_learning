
# Sources : Algorithms and Data Structures in Python (by Holczer Balazs on Udemy)

# Palindrome problem overview

# "A palindrome is a string that reads the same forward and backward"
# For example: radar or madam
# Our task is to design an optimal algorithm for checking whether a given string is palindrome or not! 

from ReverseArray import reverse

# O(N) linear running time complexity
def is_palindrome(string):

    original = string
    reversed = ''.join(reverse(list(string)))

    if original == reversed:
        return True

    return False


if __name__ == '__main__':
    print(is_palindrome('Kevin'))
    print(is_palindrome('radar'))