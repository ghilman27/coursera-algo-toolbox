"""
    DEFINE RECURRENCE PROBLEM
    min_coins(value) = 1 + min( [get_change(value - denom) for denom in DENOMINATIONS] )
    where 1 represent the last denom to be added in the change

    OPTIMAL SUBPROBLEM STRUCTURE
    suppose previous value (value - denom) has multiple combination of change's coins:
    (combination1, combination2, combination3) with length (len1, len2, len3)

    the current combination (value) would be:
    (combination1.append(denom), combination2.append(denom), combination3.append(denom))
    with length (len1+1, len2+1, len3+1)

    let's say the combination with minimum number of coins is combination2 with length (len2)

    so, the combination with minimum number of coins can only be achieved by appending denom to
    the previous combination with THE LEAST amount of coins tooo. In this case, appending 
    denom to combination2
    [.....combination2, last_value] --> last_value = denom
"""
import sys

sys.setrecursionlimit(100000)

DENOMINATIONS = [1, 3, 4]

def save_prev_change(func):
    saved_value = {}
    def save_value(*args, **kwargs):
        if args not in saved_value:
            saved_value[args] = func(*args, **kwargs)
        return saved_value[args]

    return save_value


@save_prev_change
def get_change(value):
    # base case (when value is 0, no coins for change)
    if value == 0:
        return 0
    
    crnt_num_coins = sys.maxsize
    for denom in DENOMINATIONS:
        if denom <= value:
            prev_num_coins = get_change(value - denom)
            if prev_num_coins < crnt_num_coins:
                crnt_num_coins = prev_num_coins + 1

    return crnt_num_coins
    

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
