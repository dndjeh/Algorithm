def solution(arr, divisor):
    answer = []
    bol = False
    for i in arr :
        if i%divisor == 0 :
            answer.append(i)
            bol = True
    
    if not bol:
        answer.append(-1)
    print(answer)
    return sorted(answer)



def solution(arr, divisor): return sorted([n for n in arr if n%divisor == 0]) or [-1]