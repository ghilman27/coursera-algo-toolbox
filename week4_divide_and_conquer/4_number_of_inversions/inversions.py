# Uses python3
import sys

MAX_INPUT = 10000
sys.setrecursionlimit(MAX_INPUT)


def mergesort_and_count(array, left, mid, right):
    number_of_inversions = 0
    sorted_array = []
    left_idx = left
    right_idx = mid

    while left_idx != mid and right_idx != right:
        if array[left_idx] <= array[right_idx]:
            sorted_array.append(array[left_idx])
            left_idx += 1
        else:
            sorted_array.append(array[right_idx])
            right_idx += 1

            # --KEY POINT--
            # [3 5 7 8]  [4 5 9]
            # if 5>4, then the rest (7,8) > 4, thus
            # there will be len(5,7,8) --> 3 inversions
            # or difference between mid_index and index_5
            number_of_inversions += mid-left_idx
    
    while left_idx != mid:
        sorted_array.append(array[left_idx])
        left_idx += 1
        
    while right_idx != right:
        sorted_array.append(array[right_idx])
        right_idx += 1

    array[left:right] = sorted_array
    return number_of_inversions


def get_number_of_inversions(array, left, right):
    number_of_inversions = 0
    if right - left <= 1:
        return number_of_inversions
    mid = (left + right) // 2
    number_of_inversions += get_number_of_inversions(array, left, mid)
    number_of_inversions += get_number_of_inversions(array, mid, right)
    number_of_inversions += mergesort_and_count(a, left, mid, right)
    return number_of_inversions


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    print(get_number_of_inversions(a, 0, len(a)))
