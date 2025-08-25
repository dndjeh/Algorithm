def solution(s):
    answer = True
    p_count = s.count('p')
    P_count = s.count('P')
    y_count = s.count('y')
    Y_count = s.count('Y')

    answer = True if p_count + P_count + y_count + Y_count == 0 or p_count + P_count == y_count + Y_count else False

    return answer

print(solution("Pyy"))

def numPY(s):
    # 함수를 완성하세요
    return s.lower().count('p') == s.lower().count('y')