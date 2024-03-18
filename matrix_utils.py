def transpose_matrix(matrix):
    row, col = len(matrix), len(matrix[0])
    res = [[0 for _ in range(row)] for _ in range(col)]
    for r in range(row):
        for c in range(col):
            res[c][r] = matrix[r][c]
    return res
