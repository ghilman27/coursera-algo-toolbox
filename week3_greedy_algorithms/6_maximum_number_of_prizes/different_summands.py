# Uses python3
import sys

def optimal_summands(total_candy):
    summands = []
    num_candy = 1
    candy_left = total_candy
    while True:
        if candy_left - num_candy > num_candy:
            candy_left -= num_candy
            summands.append(num_candy)
            num_candy += 1
        else:
            summands.append(candy_left)
            return summands

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
