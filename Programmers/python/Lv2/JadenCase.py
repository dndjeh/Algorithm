def solution(s):
    answer = ''
    s = s.lower()
    
    a=False
    for i in range(len(s)):
        if s[i] == ' ':
            answer += s[i]
            a = True
        elif i == 0 and (s[i]>='a' and s[i]<='z'):
            answer += chr(ord(s[i])-32)
            
        elif a and (s[i]>='a' and s[i]<='z'):
            answer += chr(ord(s[i])-32)
            a = False
        else :
            answer += s[i]
            a = False
    
    return answer

print(solution("3people unFollowed me"))