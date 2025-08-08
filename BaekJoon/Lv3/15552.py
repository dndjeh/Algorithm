import sys

temp = int(sys.stdin.readline().rstrip())

for _ in range(temp) :
    a,b = map(int, sys.stdin.readline().split())
    print(a+b)