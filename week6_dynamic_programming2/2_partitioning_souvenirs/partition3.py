import sys


def memoize(func):
    saved_value = {}
    def save_value(*args, **kwargs):
        souvenirs, capacity_A, capacity_B, capacity_C, n = args
        key = (capacity_A, capacity_B, capacity_C, n)
        if key not in saved_value:
            saved_value[key] = func(*args, **kwargs)
        return saved_value[key]

    return save_value


@memoize
def is_partitionable(souvenirs, capacity_A, capacity_B, capacity_C, n):
    # if there are no souvenirs left
    # then all the souvenirs already distributed, hence we successfully solve the problem
    if n < 0:
        return 1

    # base case
    # if all 3 partitions are completely filled (the capacities are all equal zero)
    # hence we successfully solved the problem
    if capacity_A == 0 and capacity_B == 0 and capacity_C == 0:
        return 1
    
    # if there are still capacities left in the partitions
    # there are 3 choices:
    # fill the A partition with current souvenir
    if capacity_A >= souvenirs[n]:
        first_choice_safe = is_partitionable(
            souvenirs, capacity_A-souvenirs[n], capacity_B, capacity_C, n-1
            )
        if first_choice_safe:
            return 1

    # fill the B partition with current souvenir
    if capacity_B >= souvenirs[n]:
        second_choice_safe = is_partitionable(
            souvenirs, capacity_A, capacity_B-souvenirs[n], capacity_C, n-1
            )
        if second_choice_safe:
            return 1

    # fill the C partition with current souvenir
    if capacity_C >= souvenirs[n]:
        third_choice_safe = is_partitionable(
            souvenirs, capacity_A, capacity_B, capacity_C-souvenirs[n], n-1
            )
        if third_choice_safe:
            return 1
    
    # if none of 3 choices are safe, then these souvenirs are not partitionable
    # (cannot distributed evenly)
    return 0
    

def partition3(souvenirs):
    if sum(souvenirs) % 3 != 0:
        return 0
    else:
        capacity_A = capacity_B = capacity_C = sum(souvenirs)//3
        crnt_souvenirs_idx = len(souvenirs) - 1
        return is_partitionable(
            souvenirs, capacity_A, capacity_B, capacity_C, crnt_souvenirs_idx
            )


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *S = list(map(int, input.split()))
    print(partition3(S))

