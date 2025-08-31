def solution(n):
    answer = []
    for i in str(n):
        answer.append(int(i))
    return answer[::-1]


def solution2(n):
    return [int(i) for i in str(n)][::-1]

print(solution2(1234))