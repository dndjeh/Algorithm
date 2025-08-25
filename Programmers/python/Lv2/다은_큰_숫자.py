def solution(n):
    answer = 0
    arr = []
    a=n
    while n!=0 :
        arr.append(n%2)
        n = n//2
    
    count = arr.count(1)
    
    for i in range(a+1,1000001):
        arr = []
        answer = i
        while i!=0 :
            arr.append(i%2)
            i = i//2
        if count == arr.count(1):
            break

    return answer

print(solution(15))