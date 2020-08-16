# Uses python3

START_PATTERN = [0, 1]
BASIS_MODULO = 10

def squared_pisano_sequence_and_period(m):
    if m < 2:
        print("WRONG INPUT")

    period = 0
    sequence = [0, 1]
    while True:
        sequence.append( sum(sequence[-2:]) % m )
        period += 1
        if sequence[-2:] == START_PATTERN:
            sequence = [value ** 2 % m for value in sequence]
            return sequence[:-2], period


def get_cumsum_of_squared_pisano_sequence_and_period(m):
    if m < 2:
        print("WRONG INPUT")

    PISANO_SEQUENCE, _ = squared_pisano_sequence_and_period(m)
    sequence = [0, 1]
    period = 0
    cumsum = 1
    idx = 1
    
    while True:
        idx = (idx + 1) % len(PISANO_SEQUENCE)
        period += 1
        cumsum = (cumsum + PISANO_SEQUENCE[idx]) % m
        sequence.append( cumsum )
        if sequence[-2:] == START_PATTERN:
            return sequence[:-2], period


def fibonacci_sum_squares_last_digit(n):
    sequence, period = get_cumsum_of_squared_pisano_sequence_and_period(BASIS_MODULO)
    return sequence[n % period]


if __name__ == '__main__':
    n = int(input())
    print(fibonacci_sum_squares_last_digit(n))
