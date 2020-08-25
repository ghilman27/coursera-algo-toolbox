# Uses python3
import sys
# from test import test, boyer_moore_solution, sorting_solution

MAX_INPUT = 10000
sys.setrecursionlimit(MAX_INPUT)


def partition_and_count(array, left, right):
    # if partition only has an element
    if left + 1 == right:
        return (array[left], 1)

    mid = (right - left) // 2 + left
    left_majority, left_count = partition_and_count(array, left, mid)
    right_majority, right_count = partition_and_count(array, mid, right)

    # if both has the same majority element, just add the count and return it
    if left_majority == right_majority:
        return (left_majority, left_count+right_count)
    left_count = sum(array[index] == left_majority for index in range(left, right))
    right_count = sum(array[index] == right_majority for index in range(left, right))

    # if differ, return the majority value with the greatest count
    # on the combined left and right partition
    if left_count > right_count:
        return left_majority, left_count
    else:
        return right_majority, right_count


def get_majority_element(array, left, right):
    _, count = partition_and_count(array, left, right)
    if count > right/2:
        return 1
    else:
        return -1


if __name__ == '__main__':
    # test(get_majority_element, sorting_solution)
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)
