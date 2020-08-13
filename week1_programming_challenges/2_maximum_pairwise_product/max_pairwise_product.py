# python3
# from test import test_solution

def find_two_biggest_numbers(numbers):
    first_index = 0
    second_index = 0

    for index, number in enumerate(numbers):
        if number > numbers[first_index]:
            first_index = index

    if first_index == 0:
        second_index += 1 
    for index, number in enumerate(numbers):
        if number > numbers[second_index] and index != first_index:
            second_index = index
    
    return [numbers[first_index], numbers[second_index]]


def max_pairwise_product(numbers):
    biggest_number, second_biggest_number = find_two_biggest_numbers(numbers)
    return biggest_number * second_biggest_number


if __name__ == '__main__':
    # test_solution(max_pairwise_product)
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product(input_numbers))
