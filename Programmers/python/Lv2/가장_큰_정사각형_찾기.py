def solution(board):
    answer = 0
    n = len(board) # 행
    m = len(board[0]) #열
    # 왼(j-1) 위(i-1) 대각선(i-1,j-1)
    for i in range(1,n):
        for j in range(1,m):
            if board[i][j] == 0:
                continue
            elif board[i-1][j] == 0 : # 위
                continue
            elif board[i][j-1] == 0 : # 왼
                continue
            elif board[i-1][j-1] == 0: # 왼쪽 대각선
                continue
            
            board[i][j] = min(board[i-1][j], board[i][j-1],board[i-1][j-1]) + 1

    answer = int(max(map(max, board)))**2  # 혹은 순회 중에 최대값 갱신
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    print('Hello Python')

    return answer

print(solution([[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]]))