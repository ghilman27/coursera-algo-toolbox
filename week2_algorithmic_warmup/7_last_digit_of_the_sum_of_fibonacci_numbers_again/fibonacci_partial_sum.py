# Uses python3

START_PATTERN = [0, 1]
BASIS_MODULO = 10

def get_pisano_sequence_and_period(m):
    if m < 2:
        print("WRONG INPUT")

    period = 0
    sequence = [0, 1]
    while True:
        sequence.append( sum(sequence[-2:]) % m )
        period += 1
        if sequence[-2:] == START_PATTERN:
            return sequence[:-2], period


def get_cumsum_pisano_sequence_and_period(m):
    if m < 2:
        print("WRONG INPUT")

    PISANO_SEQUENCE, _ = get_pisano_sequence_and_period(m)
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


def fibonacci_partial_sum_last_digit(from_, to):
    if from_ > to or from_ < 0 or to < 0:
        print("INVALID INPUT")
    
    sequence, period = get_cumsum_pisano_sequence_and_period(BASIS_MODULO)

    cumsum_from = 0
    if from_ > 0:
        cumsum_from = sequence[(from_ - 1) % period]
    cumsum_to = sequence[to % period]

    return (cumsum_to - cumsum_from) % BASIS_MODULO


if __name__ == '__main__':
    from_, to = map(int, input().split())
    print(fibonacci_partial_sum_last_digit(from_, to))