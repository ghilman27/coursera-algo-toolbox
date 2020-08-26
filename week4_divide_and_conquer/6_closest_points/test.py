import random
import gc
from collections import namedtuple

Point = namedtuple('Point', 'x y')
MIN_INPUT = 2
MAX_INPUT = 10000
MIN_VALUE = -100000000
MAX_VALUE = 100000000


def test(my_func, reference_func):
    while True:
        n = random.randint(MIN_INPUT, MAX_INPUT)
        x = [random.randint(MIN_VALUE, MAX_VALUE) for _ in range(n)]
        y = [random.randint(MIN_VALUE, MAX_VALUE) for _ in range(n)]
        points = list(map(lambda d: Point(d[0], d[1]), zip(x, y)))
        reference_points = points.copy()
        optimized_points = points.copy()

        reference_solution = reference_func(reference_points, n)
        optimized_solution = my_func(optimized_points, n)

        print(f"input: length {n}")
        print(f"x: {' '.join(map(str, x))}")
        print(f"y: {' '.join(map(str, y))}")
        if abs(reference_solution - optimized_solution) < 0.001:
            print("OK")
        else:
            print("ERROR")
            print(f"reference solution: {reference_solution}")
            print(f"optimized solution: {optimized_solution}")
            break

        gc.collect()
