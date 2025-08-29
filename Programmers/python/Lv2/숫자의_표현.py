def solution(n):
    answer = 0
    
    for i in range(1,int(n/2)+1):
        sum = 0
        while sum <= n :
            sum += i
            i+=1
            if sum == n :
                answer+=1
            elif sum>n:
                break
            


    return answer+1

print(solution(15))
print(int(15/2))