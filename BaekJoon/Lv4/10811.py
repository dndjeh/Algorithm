import sys

N, M = map(int, sys.stdin.readline().split())
arr = [i for i in range(1, N+1)] 

for i in range(N):
    arr[i] = i+1

for _ in range(M):
    i, j = map(int, sys.stdin.readline().split())
    arr[i-1:j] = arr[i-1:j][::-1]

print(*arr)