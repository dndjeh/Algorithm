def solution(n):
    answer = 0
    for i in range(1,int(n**(1/2))+1):
        if n == 0 :
            return 0
        
        elif n%i == 0:
            if i == n//i :
                answer += i
            else :
                answer += i
                answer += n//i

    return answer

print(solution(4))