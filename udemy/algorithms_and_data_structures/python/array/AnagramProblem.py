
# Sources : Algorithms and Data Structures in Python (by Holczer Balazs on Udemy)

# Anagram problem

# Construct an algorithm to check whether two words (or phrases) are anagrams or not!

# "An anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
# typically using all the original letters exactly once"
# For example: restful and fluster

def is_anagram(str1, str2):

    # if the length of the strings differ, they are not anagrams
    if len(str1) != len(str2):
        return False

    # sort the letters of the strings to compare - O(NlogN) running time
    str1 = sorted(str1)
    str2 = sorted(str2)

    # check the letters with the same indexes - O(N) running time
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            return False

    # overall running time is O(NlogN)+O(N)=O(NlogN)
    return True


if __name__ == '__main__':

    str1 = list('fluster')
    str2 = list('restful')

    print(is_anagram(str1, str2))
