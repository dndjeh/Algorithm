def solution(d, budget):

    d.sort()
    cnt =0
    for idx,i in enumerate(d):
        if cnt+i <= budget:
            cnt +=i
        else:
            return idx
    
    return len(d)

print(solution([2,2,3,3],10))