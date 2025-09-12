def solution(arr1, arr2):
    answer = []
    for i in range(len(arr1)):
        tmp = []
        for j in range(len(arr2[0])):
            cnt=0
            for k in range(len(arr2)):
                cnt += arr1[i][k] * arr2[k][j]
            tmp.append(cnt) 
        answer.append(tmp)
    return answer

print(solution([[2, 3, 2], [4, 2, 4], [3, 1, 4]], [[5, 4, 3], [2, 4, 1], [3, 1, 1]]))