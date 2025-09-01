import math
def solution(n, k):
    answer = list(range(1, n+1)) 
    front_arr = []
    k -= 1
    ## 첫번째 자리 수 변경 방법은 (n-1)!
    ### 계속해서 (n-1)!, (n-2)! 순서로 내려가기 만약 몫이 0이라면 다음 자릿수(n-i)!
    ### 몫이 인덱스이고, 해딩 인덱스번째가 헤딩 자릿수의 값
    for i in range(1,n): # (n-i)
        fact = math.factorial(n-i)
        front_arr.append(answer[k//fact])
        answer.remove(answer[k//fact])
        k = k%fact
        


    return front_arr + answer

print(solution(5,56))