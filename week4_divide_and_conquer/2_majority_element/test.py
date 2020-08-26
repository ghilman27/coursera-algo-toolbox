from random import randint
import gc


MIN_INPUT = 1
MAX_INPUT = 100#00
MIN_VALUE = 0
MAX_VALUE = 10#00000000


# Time Complexity: O(n log n)
# Space Complexity: O(n) --> because we assign a variable to store the sorted array
def sorting_solution(array, left, length):
    sorted_array = sorted(array)

    # -KEY POINT-
    # Theoretically, if there exists element with more than n/2 occurences
    # when we sort the array, the n/2th element will be that element
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

    # -KEY POINT-
    # Theoretically
    # if there exists element with more than or equal n/2 occurences
    # if we maintain the count
    # add it when the same value found, subtract it when differ, change it when count = 0
    # then that element is the suffix of below iteration (majority_value)
    # example [5 7 5 7 5] (output 5)
    for value in array:
        if count == 0:
            majority_value = value
        if majority_value == value:
            count += 1
        else:
            count -= 1
    
    # the above iteration can't differentiate
    # array which has two values with equal occurences
    # [7 5 7 5] (output 7)
    # and also they can't differentiate this case
    # [7 5 7 5 1] (output 1)
    # so we need to make sure the majority value occurences are more than n/2
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