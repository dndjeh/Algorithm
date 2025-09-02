def solution(s):
    answer = ''
    s = s.split(' ')
    max_num = int(s[0])
    min_num = int(s[0])
    for i in s:
        max_num = max(int(i),max_num)
        min_num = min(int(i),min_num)
    answer = str(min_num) + ' ' + str(max_num)
    return answer


a = '-1 2 3'
print(a.split(' '))