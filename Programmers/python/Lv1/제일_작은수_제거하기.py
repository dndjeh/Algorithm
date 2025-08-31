def solution(arr):
    if len(arr) ==1:
        return [-1]
    else:
        min_num = min(arr)
        
        for idx, i in enumerate(arr):
            if min_num == i:
                return arr[:idx] + arr[idx+1:]

print(solution([4,2,6]))