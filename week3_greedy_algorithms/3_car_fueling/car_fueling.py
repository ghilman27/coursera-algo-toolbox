# python3
import sys


def compute_min_refills(distance, tank, stops):
    num_of_stops = 0
    last_stop = 0
    prev_checkpoint = 0
    stops.append(distance)
    for current_checkpoint in stops:
        if current_checkpoint - prev_checkpoint > tank:
            return -1
        elif current_checkpoint - last_stop > tank:
            last_stop = prev_checkpoint
            num_of_stops += 1
        prev_checkpoint = current_checkpoint
    
    return num_of_stops


if __name__ == '__main__':
    d, m, _, *stops = map(int, sys.stdin.read().split())
    print(compute_min_refills(d, m, stops))
