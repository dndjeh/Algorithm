import math
def solution(n):
    answer = 0
    is_prime = [True]*(n+1)
    is_prime[0] = False
    is_prime[1] = False
    for i in range(2, (n+1)//2):
        if is_prime[i] == False:
            continue
        a=2
        while i*a <= n :
            if is_prime[i*a] :
                is_prime[i*a] = False
            a+=1

    return is_prime.count(True)

print(solution(10))

def solution(n):
    is_prime = [True] * (n+1)
    is_prime[0] = False
    is_prime[1] = False

    # √n까지만 확인
    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            # i의 배수를 지움 (i*i부터 시작하면 중복 제거 가능)
            for j in range(i*i, n+1, i):
                is_prime[j] = False

    return is_prime.count(True)