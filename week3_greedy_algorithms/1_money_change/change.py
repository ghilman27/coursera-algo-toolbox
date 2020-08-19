# Uses python3

def get_change(coin_value):
    DENOMINATIONS = [10, 5, 1]
    min_num_coins = 0
    for denom in DENOMINATIONS:
        while denom <= coin_value:
            coin_value -= denom
            min_num_coins += 1
    
    return min_num_coins
            


if __name__ == '__main__':
    m = int(input())
    print(get_change(m))
