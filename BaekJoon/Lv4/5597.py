import sys

arr = list(0 for i in range(0,30))

for i in range(28):
    n = int(sys.stdin.readline())
    arr[n-1] = 1


for i in range(len(arr)):
    if arr[i] == 0:
        print(i+1)