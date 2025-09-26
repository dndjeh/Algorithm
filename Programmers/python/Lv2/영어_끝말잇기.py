def solution(n, words):
    answer = []
    arr = []
    for idx, i in enumerate(words):
        if not arr :
            arr.append(i) 

        elif i in arr or arr[-1][-1] != i[0]:            
            answer.append((idx%n)+1)    # 사람 번호
            answer.append((idx//n)+1)   # 차례
            break

        elif i not in arr:
            arr.append(i)   
            if len(arr) == len(words):
                return [0,0]

    return answer

print(solution(2,["hello", "one", "eaven", "never", "now", "world", "draw"]))