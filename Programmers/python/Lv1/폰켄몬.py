def solution(nums):
    answer = 0
    N = len(nums)
    bol = [False]*N
    for i in range (N):
        if not bol[i] and answer < (N/2) :
            answer += 1
            bol[i] = True
            for j in range(i+1, N):
                if nums[i] == nums[j]:
                    bol[j] = True
        
    return print(answer)


def solution2(nums):
    return print(min(len(nums)/2, len(set(nums))))

nums = [1,1,1,3,3,4]
solution2(nums)