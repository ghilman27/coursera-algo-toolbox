# Uses python3
# from test import test

def calc_fib(n):
    if (n <= 1):
        return n
    
    prev_fib_numbers = [0, 1]
    current_fib_number = None
    for _ in range(2,n+1):
        current_fib_number = sum(prev_fib_numbers)
        prev_fib_numbers = [prev_fib_numbers[-1], current_fib_number]
    return current_fib_number


# test(calc_fib)
n = int(input())
print(calc_fib(n))