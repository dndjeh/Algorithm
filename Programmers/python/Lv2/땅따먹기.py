def solution(land):
    answer = 0
    n = len(land)   #행 
    m = len(land[0])#열
    for i in range(1,n):
        for j in range(m):
            result = land[i][j]
            for k in range(m):
                if j != k:
                    land[i][j] = max(land[i][j], land[i-1][k]+result)

    answer = max(land[-1])
    return answer


def solution2(land):
    for i in range(1, len(land)):
        for j in range(len(land[0])):
            land[i][j] = max(land[i -1][: j] + land[i - 1][j + 1:]) + land[i][j]

    return max(land[-1])

print(solution([[1,2,3,5],
                [5,6,7,8],
                [4,3,2,1]]))