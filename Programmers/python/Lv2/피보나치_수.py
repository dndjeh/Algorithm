visited = [False] * (100001)
arr = [0]*(100001)

def solution(n):
    if n == 0:
        visited[0] = True
        return 0
    elif n == 1:
        visited[1] = True
        return 1
    
    elif  visited[n] == False :
        visited[n] = True
        arr[n] = solution(n-2) + solution(n-1)

    elif visited[n] :
        return arr[n]%1234567

    return arr[n]%1234567

print(solution(3))

def solution(n):
    a, b = 0, 1
    for _ in range(2, n+1):
        a, b = b, (a + b) % 1234567  # 항상 작은 수 유지
    return b
