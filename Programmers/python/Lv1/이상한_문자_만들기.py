def solution(s):
    answer = ''
    cnt = 0
    for i in range(len(s)) :
        if s[i] == ' ':
            answer += ' '
            cnt = 0
            continue
        elif cnt%2 == 0:
            answer += s[i].upper()
        else :
            answer += s[i].lower()
        cnt +=1
    return answer

def toWeirdCase(s):
    a=[]
    s=s.split(" ")
    for i in range(len(s)):
        for j in range(len(s[i])):
            if j%2==0:
                a.append(s[i][j].upper())
            else:
                a.append(s[i][j].lower())
        a.append(" ")

    c="".join(a[:-1])
    return c

print(toWeirdCase('try hello world'))