import re
def solution(s):
    if not re.search('[a-zA-Z]',s) and (len(s) ==4 or len(s)==6):
        return True
    
    return False

print(solution('1234'))

def alpha_string46(s):
    #함수를 완성하세요

    return s.isdigit() and len(s) in [4,6]