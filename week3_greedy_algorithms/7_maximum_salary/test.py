import random
import gc

MIN_VALUE = 1
MAX_VALUE = 1000

def naive_solution(a, b):
    num1 = int(str(a) + str(b))
    num2 = int(str(b) + str(a))
    if num1 > num2:
        return a
    else:
        return b

def test(my_func):
    while True:
        a = random.randint(MIN_VALUE, MAX_VALUE)
        b = random.randint(MIN_VALUE, MAX_VALUE)
        reference_solution = naive_solution(a, b)
        optimized_solution = my_func(a, b)

        print(f"a: {a}, b: {b}")
        if reference_solution == optimized_solution:
            print("OK")
        else:
            print("ERROR")
            print(f"reference solution: {reference_solution}")
            print(f"optimized solution: {optimized_solution}")
            break

        gc.collect()