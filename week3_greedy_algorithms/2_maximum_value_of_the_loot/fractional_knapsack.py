# Uses python3
import sys

def sort_densities(weights, values):
    densities = [value * 1.0 / weight for weight, value in zip(weights, values)]
    return sorted([(density, index) for index, density in enumerate(densities)], reverse=True)


def get_optimal_value(capacity, weights, values):
    value = 0.
    sorted_densities = sort_densities(weights, values)

    for item_density, item_index in sorted_densities:
        if weights[item_index] <= capacity:
            capacity -= weights[item_index]
            value += values[item_index]
        else:
            value += capacity * item_density
            return value
    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print(f"{opt_value:.4f}")