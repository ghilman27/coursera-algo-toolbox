"""
    RECURRENCE PROBLEM
    optimal_sequence(value) = min([len(optimal_sequence(value modified_by operator) for operator in OPERATORS)]) + 1
    where OPERATORS is +1, x2, or x3

    BASE CASE
    where value equal to 0, return zero

    OPTIMAL SUBPROBLEM STRUCTURE
    the same as money change problem, but now we have 3 operator instead of +1
"""
import sys
sys.setrecursionlimit(10000)


def memoize(func):
    saved_value = {}
    def save_value(*args, **kwargs):
        if args not in saved_value:
            saved_value[args] = func(*args, **kwargs)
        return saved_value[args]

    return save_value


@memoize
def optimal_sequence(n):
    if n == 0:
        return []
    
    crnt_seq = []
    if n % 3 == 0:
        prev_seq = optimal_sequence(n // 3)
        if len(crnt_seq) == 0 or len(prev_seq) < len(crnt_seq):
            crnt_seq = prev_seq.copy()
            crnt_seq.append(n)
    if n % 2 == 0:
        prev_seq = optimal_sequence(n // 2)
        if len(crnt_seq) == 0 or len(prev_seq) < len(crnt_seq):
            crnt_seq = prev_seq.copy()
            crnt_seq.append(n)

    prev_seq = optimal_sequence(n - 1)
    if len(crnt_seq) == 0 or len(prev_seq) < len(crnt_seq):
        crnt_seq = prev_seq.copy()
        crnt_seq.append(n)
    
    return crnt_seq


def optimal_sequence_iteration(n):
    sequences = [[]] * (n+1)

    for value in range(1, n+1):
        if value == 1:
            sequences[value] = [1]
        else:
            crnt_seq = sequences[value]
            if value % 3 == 0:
                prev_seq = sequences[value // 3]
                if len(crnt_seq) == 0 or len(prev_seq) < len(crnt_seq):
                    crnt_seq = prev_seq.copy()
                    crnt_seq.append(value)
            if value % 2 == 0:
                prev_seq = sequences[value // 2]
                if len(crnt_seq) == 0 or len(prev_seq) < len(crnt_seq):
                    crnt_seq = prev_seq.copy()
                    crnt_seq.append(value)
            prev_seq = sequences[value - 1]
            if len(crnt_seq) == 0 or len(prev_seq) < len(crnt_seq):
                crnt_seq = prev_seq.copy()
                crnt_seq.append(value)

            sequences[value] = crnt_seq.copy()

    return sequences[n]


if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    sequence = list(optimal_sequence_iteration(n))
    print(len(sequence) - 1)
    for x in sequence:
        print(x, end=' ')
