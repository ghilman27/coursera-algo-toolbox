# Uses python3
import gc
from random import randint

def naive_solution(n):
    if (n <= 1):
        return n

    return naive_solution(n - 1) + naive_solution(n - 2)


def formula_solution(n):
    # only valid to n <= 71 due to approximation error
    if (n <= 1):
        return n
    
    Phi = (1 + 5**0.5) / 2
    phi = -1/Phi

    return int((Phi**n - phi**n) / 5**0.5)


def list_solution(n):
    if (n <= 1):
        return n
    
    fib_array = [0, 1]
    for index in range(2,n+1):
        fib_array.append(fib_array[index-1] + fib_array[index-2])
    return fib_array[n]


def test(my_func):
    MIN_N_VALUE = 0
    MAX_N_VALUE = 45

    while True:
        n = randint(MIN_N_VALUE, MAX_N_VALUE)
        reference_solution = formula_solution(n)
        optimized_solution = my_func(n)

        print(f"n: {n}")
        if reference_solution == optimized_solution:
            print("OK")
        else:
            print("ERROR")
            print(f"reference solution: {reference_solution}")
            print(f"optimized solution: {optimized_solution}")
            break

        gc.collect()