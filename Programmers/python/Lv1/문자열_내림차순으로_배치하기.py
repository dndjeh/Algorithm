def solution(s):
    a = ''.join(sorted(s,reverse=True))
    
    return a

print(solution('Zbcadefg'))