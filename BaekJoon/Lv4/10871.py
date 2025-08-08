N, X = map(int, input().split())
arr = list(map(int, input().split()))

if len(A) != N:
    raise ValueError("입력된 수열의 개수가 N과 다릅니다.")

for i in range(len(arr)):
    if arr[i] < X:
        print(arr[i], end=' ')