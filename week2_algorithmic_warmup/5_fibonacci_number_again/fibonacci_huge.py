# Uses python3

def get_pisano_sequence_and_period(m):
    if m < 2:
        print("WRONG INPUT")

    period = 0
    sequence = [0, 1]
    while True:
        sequence.append( sum(sequence[-2:]) % m )
        period += 1
        if sequence[-2:] == [0, 1]:
            return sequence[:-2], period


def get_fibonacci_huge(n, m):
    sequence, period = get_pisano_sequence_and_period(m)
    return sequence[n % period]


if __name__ == '__main__':
    n, m = map(int, input().split())
    print(get_fibonacci_huge(n, m))
