def solution(matrix):
    n = len(matrix)     # 행 갯수
    m = len(matrix[0])  # 열 갯수
    
    # 하, 우, 좌, 상 이동
    dx = [1, 0, 0, -1] # 행 
    dy = [0, 1, -1, 0] # 열

    # 현재 위치 저장
    q = []
    q.append((0,0))

    # 주변을 탐색하면서 마지막 좌표까지 이동 => BFS 탐색
    # 주변으로 이동할 수 없는 경우 => 결국 마지막 좌표에서 종료
    while len(q) > 0:
        pos = q.pop(0)

        # 하, 우, 좌, 상 이동
        for i in range(4):
            nx = pos[0] + dx[i]
            ny = pos[1] + dy[i]

            # 맵을 벗어날 경우
            if not (0 <= nx < n) or not (0 <= ny < m):
                continue
                
            # 시작 지점으로 돌아갈 경우
            if nx == 0 and ny == 0:
                continue

            # 벽을 만날 경우
            if matrix[nx][ny] == 0:
                continue

            # 가중치가 정해지지 않았을 경우
            if matrix[nx][ny] == 1:
                matrix[nx][ny] += matrix[pos[0]][pos[1]]
                
                # 다음 이동 위치를 q에 담는다
                q.append((nx, ny))
            # 가중치가 정해져있을 경우
            else:
                matrix[nx][ny] = min(matrix[nx][ny], matrix[pos[0]][pos[1]] + 1)
            				
    # 마지막 위치가 도달 불가능하면
    if matrix[n-1][m-1] == 1:
        return -1
    
    # 마지막 좌표의 가중치를 반환
    return matrix[n-1][m-1]




def solution2(maps):
    n = len(maps)
    m = len(maps[0])
    
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    q= []
    q.append((0,0))

    while len(q) > 0 :
        pos = q.pop()
        
        for i in range(4):
            nx = pos[0] + dx[i]
            ny = pos[1] + dy[i]

            # 범위 벗어남
            if not (0<= nx < n) or not(0<= ny < m):
                continue

            # 0인 경우
            if maps[nx][ny] == 0 :
                continue

            # 1인경우
            if maps[nx][ny] == 1 :
                maps[nx][ny] += maps[pos[0]][pos[1]]
                q.append((nx,ny))

            # 2 이상인 경우
            else:
                maps[nx][ny] = min(maps[nx][ny], maps[pos[0]][pos[1]]+1)
    
    if maps[n-1][m-1] == 1:
        return -1
    
    return maps[n-1][m-1]



maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]

print(solution2(maps))