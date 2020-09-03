from Levenshtein import distance
from string import ascii_lowercase
import random
import gc

MIN_LENGTH = 1
MAX_LENGTH = 100


def test(my_func):
    while True:
        s_length = random.randint(MIN_LENGTH, MAX_LENGTH)
        t_length = random.randint(MIN_LENGTH, MAX_LENGTH)
        s = ''.join(random.choice(ascii_lowercase) for _ in range(s_length))
        t = ''.join(random.choice(ascii_lowercase) for _ in range(t_length))

        reference_solution = distance(s, t)
        optimized_solution = my_func(s, t)

        print(f"s: {s}")
        print(f"t: {t}")
        if reference_solution == optimized_solution:
            print("OK")
        else:
            print("ERROR")
            print(f"reference solution: {reference_solution}")
            print(f"optimized solution: {optimized_solution}")
            break

        gc.collect()


