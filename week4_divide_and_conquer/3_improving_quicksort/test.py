import random
import gc


MIN_INPUT = 1
MAX_INPUT = 10000
MIN_VALUE = 0
MAX_VALUE = 1000000000


def partition2(array, left, right):
    pivot_value = array[left]
    final_pivot_idx = left

    for crnt_idx in range(left + 1, right + 1):
        if array[crnt_idx] <= pivot_value:
            final_pivot_idx += 1
            array[crnt_idx], array[final_pivot_idx] = array[final_pivot_idx], array[crnt_idx]

    array[left], array[final_pivot_idx] = array[final_pivot_idx], pivot_value
    return final_pivot_idx


def randomized_quick_sort2(array, left, right):
    if left >= right:
        return

    rand_pivot_idx = random.randint(left, right)
    array[left], array[rand_pivot_idx] = array[rand_pivot_idx], array[left]
    final_pivot_idx = partition2(array, left, right)
    randomized_quick_sort2(array, left, final_pivot_idx - 1)
    randomized_quick_sort2(array, final_pivot_idx + 1, right)


def test(my_func, reference_func):
    while True:
        n = random.randint(MIN_INPUT, MAX_INPUT)
        a = [random.randint(MIN_VALUE, MAX_VALUE) for _ in range(n)]
        reference_solution = a.copy()
        optimized_solution = a.copy()
        reference_func(reference_solution, 0, n-1)
        my_func(optimized_solution, 0, n-1)

        print(f"input: length {n}\n{' '.join(map(str, a))}")
        if reference_solution == optimized_solution:
            print("OK")
        else:
            print("ERROR")
            print(f"reference solution: {reference_solution}")
            print(f"optimized solution: {optimized_solution}")
            break

        gc.collect()