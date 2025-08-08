hour, minute = map(int, input().split(' '))
time = int(input())

result = minute + time

if result >= 60 :
    hour += result/60
    minute = result%60

else :
    minute = result

if hour >=24 :
    hour = hour%24

print(int(hour), minute)
