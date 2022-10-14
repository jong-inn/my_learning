
# Sources : Algorithms and Data Structures in Python (by Holczer Balazs on Udemy)

# Dutch national flag problem

# The problem is that we want to sort a T[] one-dimensional array of integers in O(N) running time 
# and without any extra memory. The array can contain values: 0, 1 and 2
# (check out the theoretical section for further information).
# For example: [0, 1, 2, 1, 2, 0, 0] -> [0, 0, 0, 1, 1, 2, 2]

def dutch_flag_problem(arr, pivot=1):
    # i for tracking 0, j for tracking 1, k for tracking 2
    i = 0
    j = 0
    k = len(arr) - 1

    while j <= k:
        # current element is 0
        if arr[j] < pivot:
            swap(arr, i, j)
            i += 1
            j += 1
        # current element is 2
        elif arr[j] > pivot:
            swap(arr, j, k)
            k -= 1
        # current element is 1
        else:
            j += 1

    return arr


def swap(arr, idx1, idx2):
    arr[idx1], arr[idx2] = arr[idx2], arr[idx1]


if __name__ == '__main__':
    print(dutch_flag_problem([0, 1, 2, 1, 2, 0, 0]))
    print(dutch_flag_problem([0, 1, 2, 2, 1, 0, 0, 2, 2, 1]))
