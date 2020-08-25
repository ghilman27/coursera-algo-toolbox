from random import randint
import gc


MIN_INPUT = 1
MAX_INPUT = 10000
MIN_VALUE = 0
MAX_VALUE = 1000000000


# Time Complexity: O(n log n)
# Space Complexity: O(n) --> because we assign a variable to store the sorted array
def sorting_solution(array, left, length):
    sorted_array = sorted(array)
    majority_value = sorted_array[length // 2]
    count = sorted_array.count(majority_value)
    if count > length / 2:
        return 1
    return -1


# Time Complexity: O(n)
# Space Complexity: O(1)
def boyer_moore_solution(array, left, length):
    count = 0
    majority_value = None

    for value in array:
        if count == 0:
            majority_value = value
        if majority_value == value:
            count += 1
        count -= 1
    
    if array.count(majority_value) > length / 2:
        return 1
    return -1


def test(my_func, reference_func):
    while True:
        n = randint(MIN_INPUT, MAX_INPUT)
        a = [randint(MIN_VALUE, MAX_VALUE) for _ in range(n)]
        reference_solution = reference_func(a, 0, n)
        optimized_solution = my_func(a, 0, n)

        print(f"input: length {n}\n{' '.join(map(str, a))}")
        if reference_solution == optimized_solution:
            print("OK")
        else:
            print("ERROR")
            print(f"reference solution: {reference_solution}")
            print(f"optimized solution: {optimized_solution}")
            break

        gc.collect()