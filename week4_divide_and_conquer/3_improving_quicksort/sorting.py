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
        # -KEY POINT-
        # double subtitution because when left partition added, 
        # first index of middle partition will be shifted
        # [l l m m m v * *]
        # [l l v m m m * *]
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
    left_part_idx, final_pivot_idx = partition3(array, left, right)

    # -KEY POINT-
    if left_part_idx is not None:
        # if middle partition exist (there are multiple occurence of pivot number)
        # then exclude the middle partition (because they all are the same)
        # no need to be sorted
        randomized_quick_sort(array, left, left_part_idx)
    else:
        # else exclude the pivot value
        # because it is already in its final place
        randomized_quick_sort(array, left, final_pivot_idx - 1)
    randomized_quick_sort(array, final_pivot_idx + 1, right)


if __name__ == '__main__':
    # test(randomized_quick_sort, randomized_quick_sort2)
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    randomized_quick_sort(a, 0, n - 1)
    for x in a:
        print(x, end=' ')
