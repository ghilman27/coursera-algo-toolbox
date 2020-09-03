"""
    RECURRENCE WITH OPTIMAL SUBPROBLEM STRUCTURE
    we want to add item1, item2, ...., item_n
    with value v1, v2, ...., v_n and weight w1, w2, ....., w_n
    so that value is maximized and total weight added is not > Capacity (W)
    no recurrence

    suppose we want to add item_n to the knapsack.
    we can choose 2 options:
    - not taking the current item_n, so :
      + the current capacity still intact (W)
      + the current value is the same as total of value from previous item (v1+v2+....+vn-1)
    - taking the item_n, so :
      + the current capacity is reduced to (W - w_n)
      + the current value is the same as total value from previous item + v_n
    
    Each choise then will have the same branch again on and on


    APPROACH
    We can approach this problem with bottom-up iteration
    by building optimum_value_matrix
       1   2   3   4   5   6   ...   W    (Capacity)
 i  1
 t  2
 e  3
 m  4
 i  5
 d  6
 x  7

    Options:
    - taking the item: 
      the value of value_matrix[item_n][capacity_n] is the maximum of:
        value_matrix[item_n - 1][capacity_n - w_n] + v_n   <----- option if we taking the item
        value_matrix[item_n - 1][capacity_n]               <----- option if we not taking the item
    
    - not taking the item:
      value_matrix[item_n][capacity_n] = value_matrix[item_n - 1][capacity_n] 
      

    Is kinda hard to simulate this in text so just see the video
    https://www.youtube.com/watch?v=xOlhR_2QCXY
    https://www.coursera.org/learn/algorithmic-toolbox/lecture/QVEY4/knapsack-without-repetitions

"""

import sys

def optimal_weight(W, w_golds):
    rows, cols = (len(w_golds)+1, W+1)
    weight_matrix = [[0 for col in range(cols)] for row in range(rows)]

    for row, g_idx in zip(range(1, rows), range(len(w_golds))):
        for col, w in zip(range(1, cols), range(1, W+1)):
            if w_golds[g_idx] > w:
                weight_matrix[row][col] = weight_matrix[row-1][col]
            else:
                not_taking_weight = weight_matrix[row-1][col]
                taking_weight = weight_matrix[row-1][col - w_golds[g_idx]] + w_golds[g_idx]
                weight_matrix[row][col] = max(taking_weight, not_taking_weight)

    return weight_matrix[len(w_golds)][W]


if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w))
