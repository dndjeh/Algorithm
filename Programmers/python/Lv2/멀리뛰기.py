
def solution(n, arr = {}):
    if n in arr :
        return arr[n]
    
    if n > 0 :
        if n == 1:
            return 1
        elif n ==2 :
            return 2

        arr[n] = (solution(n-1,arr) + solution(n-2,arr))%1234567
        return arr[n]

print(solution(5))

def solution2(n):
    if n == 1:
        return 1
    if n == 2:
        return 2

    dp = [0] * (n+1)
    dp[1], dp[2] = 1, 2

    for i in range(3, n+1):
        dp[i] = (dp[i-1] + dp[i-2]) % 1234567

    return dp[n]
