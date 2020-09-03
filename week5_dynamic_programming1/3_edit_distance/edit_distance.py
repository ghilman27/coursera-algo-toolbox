# from test import test

def edit_distance(s, t):
    # Construct distance matrix
    rows, cols = (len(s)+1, len(t)+1)
    distance_matrix = [[0 for col in range(cols)] for row in range(rows)] 

    # fill first column and first row of the matrix,
    # corresponding to the insertion and deletion from empty character ('')
    for col in range(cols):
        distance_matrix[0][col] = col
    for row in range(rows):
        distance_matrix[row][0] = row
    
    """
    iteratively compute minimum distance represented
    by distance matrix, resulted from either:
    - subtitution of s[s_idx] with t[t_idx]
    - insertion of t[t_idx]
    - deletion of s[s_idx]

    ILUSTRATION WITH THE DISTANCE MATRIX
           ----------> insertion        
    |row-1, col-1| row-1, col| |
               \               | deletion
                \ subtitution  |
                 \             v
    | row, col-1 |  row, col |
    """
    for row, s_idx in zip(range(1, rows), range(len(s))):
        for col, t_idx in zip(range(1, cols), range(len(t))):
            cost = (s[s_idx] != t[t_idx])
            subtitution_distance = distance_matrix[row-1][col-1] + cost
            insertion_distance = distance_matrix[row][col-1] + 1
            deletion_distance = distance_matrix[row-1][col] + 1
            distance_matrix[row][col] = min(subtitution_distance, insertion_distance, deletion_distance)
    
    # return the edit distance of string `s` and string `t`
    # which is the value of the bottom-right part of edit distance matrix
    return distance_matrix[len(s)][len(t)]


if __name__ == "__main__":
    # test(edit_distance)
    print(edit_distance(input(), input()))
