N,M = map(int, input().split()) # 행, 열

matrix_A = [0 for _ in range(N)]

matrix_B = [0 for _ in range(N)]

for i in range(N):
    matrix_A[i] = (list(map(int, input().split())))

for i in range(N):
    matrix_B[i] = (list(map(int, input().split())))

for i in range(N):
    for j in range(M):
        matrix_A[i][j] += matrix_B[i][j]

for i in range(N):
    for j in range(M):
        print(matrix_A[i][j], end=' ')
    print()
