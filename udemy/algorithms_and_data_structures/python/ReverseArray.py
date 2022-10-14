
# Sources : Algorithms and Data Structures in Python (by Holczer Balazs on Udemy)

# Reversing an array in-place overview

# The problem is that we want to reverse a T[] array in O(N) linear time complexity
# and we want the algorithm to be in-place as well
# - so no additional memory can be used!

# For example: input is [1,2,3,4,5] then the output is [5,4,3,2,1]

def reverse(arr):

    # index for start and end
    start_idx = 0
    end_idx = len(arr)-1

    while end_idx > start_idx:
        # keep swapping the items
        arr[start_idx], arr[end_idx] = arr[end_idx], arr[start_idx]
        start_idx += 1
        end_idx -= 1


if __name__ == '__main__':

    n = [-3, 0, 3]
    reverse(n)
    print(n)

    n = [1, 2, 3, 4]
    reverse(n)
    print(n)