from collections import deque

def solution(s):
    q = deque(s)
    count = 0
    while q:
        ch = q.popleft()
        if ch == '(':
            count += 1
        else:  # ')'
            count -= 1
        if count < 0:
            return False
    return count == 0


print(solution("(())"))