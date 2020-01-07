# Majority Element
# Write a function which takes an array and prints the majority element (if it exists),
# otherwise prints “No Majority Element”.
# A majority element in an array A[] of size n is an element that appears more than n/2 times
# (and hence there is at most one such element).

def majorityElement(arr):
    dict = {}
    for i in (arr):
        if dict.get(i):
            dict[i] = dict.get(i) + 1
            if dict.get(i) > len(arr)// 2:
                return i
        else:
            dict[i] = 1
    return "No Majority Element"


if __name__ == '__main__':
    arr = [3, 3, 4, 2, 4, 4, 2, 4, 4]
    p
