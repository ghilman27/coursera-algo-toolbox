from random import randint
import gc

MIN_INPUT_NUMBER = 0
MAX_INPUT_NUMBER = 1000
MIN_INPUT_LENGTH = 2
MAX_INPUT_LENGTH = 1000


def built_in_solution(numbers):
    sorted_numbers = sorted(numbers, reverse=True)
    return sorted_numbers[0] * sorted_numbers[1]


def test_solution(solution_func):
    while True:
        input_length = randint(MIN_INPUT_LENGTH, MAX_INPUT_LENGTH)
        input_numbers = [randint(MIN_INPUT_NUMBER, MAX_INPUT_NUMBER) for _ in range(input_length)]
        slow_but_true_solution = built_in_solution(input_numbers)
        fast_solution = solution_func(input_numbers)

        print(f"n: {input_length}")
        print(f"input_numbers: {input_numbers}")
        if fast_solution == slow_but_true_solution:
            print("OK")
        else:
            print("ERROR")
            print(f"true solution: {slow_but_true_solution}, fast solution: {fast_solution}")
            break
        gc.collect()