def solution(n):
    ans = 0
    
    while n!=0:
        if n%2==0:
            n=int(n/2)
        else :
            ans+=1
            n = n-1
    print('Hello Python')

    return ans

print(solution(11))