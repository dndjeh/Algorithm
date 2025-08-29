def solution(s, n):
    Up = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    
    answer = ''
    for str in s :
        if str == ' ':
            answer += ' '
            continue

        for i in range(len(Up)):
            if str == Up[i]:
                if i + n > len(Up)-1:
                    answer += Up[i+n-len(Up)]
                    break
                else:
                    answer += Up[i+n]
                    break
            elif str == Up[i].lower():
                if i + n > len(Up)-1:
                    answer += Up[i+n-len(Up)].lower()
                    break
                else:
                    answer += Up[i+n].lower()
                    break

    
    return answer

print(solution('A B C D',3))

def solution2(s, n):
    answer = ''
    for i in s:
        if i:
            if i >= 'A' and i <= 'Z':
                answer += chr((ord(i) - ord('A') + n) % 26 + ord('A'))
            elif i >= 'a' and i <= 'z':
                answer += chr((ord(i) - ord('a') + n) % 26 + ord('a'))
            else : answer += ' '
    return answer

print(ord('A'))