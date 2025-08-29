def solution(begin, end):
    answer = [1] * (end - begin +1)
    for i in range(begin, end+1):
        for j in range(2, int(i**(1/2)) + 1):
            if (i % j == 0):
                if i//j <= 10000000 :
                    answer[i-begin] =  i//j
                    break
                else :
                    answer[i-begin] = j


    if begin == 1:
        answer[0] = 0   

    return answer

print(solution(1,10))