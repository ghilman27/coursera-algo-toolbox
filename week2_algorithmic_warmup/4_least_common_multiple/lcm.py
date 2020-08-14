# Uses python3

def calc_gcd(a, b):
    if a == 0:
        return b
    elif b == 0:
        return a
    
    remainder = max(a,b) % min(a,b)
    return calc_gcd(min(a,b), remainder)


def lcm(a, b):
    if a == 0 or b == 0:
        return 0

    gcd = calc_gcd(a, b)
    if gcd == 1:
        return a*b
    else:
        return int(min(a,b) / gcd) * max(a,b)


if __name__ == '__main__':
    a, b = map(int, input().split())
    print(lcm(a, b))

