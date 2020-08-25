#Uses python3

import sys
import math
# from test import test

def right_nth_digit(number, n):
    return number // 10**(n-1) % 10


def max_(num1, num2):
    max_number = max(num1,num2)
    min_number = min(num1,num2)
    max_digit = int(math.log10(max_number) + 1)
    min_digit = int(math.log10(min_number) + 1)

    if max_digit == min_digit:
        return max_number

    digit_diff = max_digit - min_digit
    max_number_first_min_digit_digits = max_number // 10**digit_diff
    if min_number > max_number_first_min_digit_digits:
        return min_number
    elif max_number_first_min_digit_digits > min_number:
        return max_number
    
    for n in range(digit_diff, 0, -1):
        if right_nth_digit(min_number, min_digit) > right_nth_digit(max_number, n):
            return min_number
        elif right_nth_digit(min_number, min_digit) < right_nth_digit(max_number, n):
            return max_number

    max_number_last_min_digit_digits = max_number % 10**min_digit
    if max_number_last_min_digit_digits > min_number:
        return min_number
    else:
        return max_number


def is_greater(num1, num2):
    return max_(num1, num2) == num1


def shift_(numbers, idx):
    if (idx != 0):
        if is_greater(numbers[idx], numbers[idx-1]):
            numbers[idx], numbers[idx-1] = numbers[idx-1], numbers[idx]
            shift_(numbers, idx-1)


def sort_(numbers):
    for idx in range(len(numbers)):
        shift_(numbers, idx)


def largest_number(numbers):
    sort_(numbers)
    result = ""
    for number in numbers:
        result += str(number)
    return result


if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    numbers = list(map(int, a))
    print(largest_number(numbers))
    # test(max_)