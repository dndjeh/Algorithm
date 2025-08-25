def solution(n):
    answer = ''.join('수박' for _ in range(10001//2))
    return answer[:n]

print(solution(10))