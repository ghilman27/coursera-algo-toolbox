# Uses python3
import sys
import random
# from test import test, randomized_quick_sort2

MAX_VALUE = 10000
sys.setrecursionlimit(MAX_VALUE)


def partition3(array, left, right):
    #write your code here
    pivot_value = array[left]
    left_part_idx = left
    final_pivot_idx = left

    for crnt_idx in range(left + 1, right + 1):
        if array[crnt_idx] < pivot_value:
            left_part_idx += 1
            final_pivot_idx += 1
            array[crnt_idx], array[left_part_idx] = array[left_part_idx], array[crnt_idx]
            if final_pivot_idx != left_part_idx:
                array[crnt_idx], array[final_pivot_idx] = array[final_pivot_idx], array[crnt_idx]
                
        elif array[crnt_idx] == pivot_value:
            final_pivot_idx += 1
            array[crnt_idx], array[final_pivot_idx] = array[final_pivot_idx], array[crnt_idx]
    
    array[left], array[final_pivot_idx] = array[final_pivot_idx], pivot_value
    if final_pivot_idx != left_part_idx:
        return left_part_idx, final_pivot_idx
    return None, final_pivot_idx


def randomized_quick_sort(array, left, right):
    if left >= right:
        return

    rand_pivot_idx = random.randint(left, right)
    array[left], array[rand_pivot_idx] = array[rand_pivot_idx], array[left]
    #use partition3
    left_part_idx, final_pivot_idx = partition3(array, left, right)
    if left_part_idx is not None:
        randomized_quick_sort(array, left, left_part_idx)
    else:
        randomized_quick_sort(array, left, final_pivot_idx - 1)
    randomized_quick_sort(array, final_pivot_idx + 1, right)


if __name__ == '__main__':
    # test(randomized_quick_sort, randomized_quick_sort2)
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    randomized_quick_sort(a, 0, n - 1)
    for x in a:
        print(x, end=' ')
