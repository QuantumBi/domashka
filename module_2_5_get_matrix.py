def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        post_matrix = []
        for j in range(m):
            post_matrix.append(value)
        matrix.append(post_matrix)
    return matrix

result1 = get_matrix(0, 0, 0)

print(result1)