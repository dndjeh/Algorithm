def solution(x):
    sum_num = 0
    a = str(x)
    for _ in range(len(a)+1):
        sum_num += (x)%10
        x = x//10
        
    if int(a)%sum_num == 0:
        return True
    else:
        return False

solution(123)