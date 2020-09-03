"""
    This is an alignment problem, a variation of edit distance problem
    best solved with Needleman–Wunsch algorithm
    we then set the weight:
    - insertion: 0
    - deletion: 0
    - mismatch: 0
    - match: 1

    and unlike edit distance who compute the minimum number of operation
    we compute the maximum number of equation
"""


import sys

def lcs2(s, t):
    # Construct distance matrix
    rows, cols = (len(s)+1, len(t)+1)
    distance_matrix = [[0 for col in range(cols)] for row in range(rows)] 

    for row, s_idx in zip(range(1, rows), range(len(s))):
        for col, t_idx in zip(range(1, cols), range(len(t))):
            match_weight = (s[s_idx] == t[t_idx])
            match = distance_matrix[row-1][col-1] + match_weight
            insertion = distance_matrix[row][col-1]
            deletion = distance_matrix[row-1][col]
            distance_matrix[row][col] = max(match, insertion, deletion)
    
    return distance_matrix[len(s)][len(t)]


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))

    n = data[0]
    data = data[1:]
    a = data[:n]

    data = data[n:]
    m = data[0]
    data = data[1:]
    b = data[:m]

    print(lcs2(a, b))
