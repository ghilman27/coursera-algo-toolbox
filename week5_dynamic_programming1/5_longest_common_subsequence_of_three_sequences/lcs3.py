"""
    The same as 2D case, we only extend the dimensions
    there are 7 possible operations and one of them is 
    matching operation (a[i] == b[j] == c[k])
    which we give weight = 1
    other operations have weight 0

    then compute the maximum operations from all 7 possibilities
"""


import sys

def lcs3(a, b, c):
    i_size, j_size, k_size = (len(a)+1, len(b)+1, len(c)+1)
    distance_matrix = [[[0 for k in range(k_size)] for j in range(j_size)] for i in range(i_size)]

    for i, a_idx in zip(range(1, i_size), range(len(a))):
        for j, b_idx in zip(range(1, j_size), range(len(b))):
            for k, c_idx in zip(range(1, k_size), range(len(c))):
                match_weight = (a[a_idx] == b[b_idx] == c[c_idx])
                match_operation = distance_matrix[i-1][j-1][k-1] + match_weight
                other_operations = [
                    distance_matrix[i-1][j][k],
                    distance_matrix[i][j-1][k],
                    distance_matrix[i][j][k-1],
                    distance_matrix[i-1][j-1][k],
                    distance_matrix[i][j-1][k-1],
                    distance_matrix[i-1][j][k-1],
                ]
                distance_matrix[i][j][k] = max([*other_operations, match_operation])
    
    return distance_matrix[len(a)][len(b)][len(c)]


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    an = data[0]
    data = data[1:]
    a = data[:an]
    data = data[an:]
    bn = data[0]
    data = data[1:]
    b = data[:bn]
    data = data[bn:]
    cn = data[0]
    data = data[1:]
    c = data[:cn]
    print(lcs3(a, b, c))
