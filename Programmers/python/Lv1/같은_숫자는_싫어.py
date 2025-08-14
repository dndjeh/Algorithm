def solution(arr):
    answer = []

    for i in range(len(arr)) :
        if len(answer)==0 or arr[i] != answer[-1] :
            answer.append(arr[i])

    return answer

def no_continuous(s):
    # 함수를 완성하세요
    a = []
    for i in s:
        if a[-1:] == [i]:
            continue
        a.append(i)
    return a

arr = [4,4,4,1,2,1,1]
print(solution(arr))
print(no_continuous(arr))