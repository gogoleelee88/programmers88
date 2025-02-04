def solution(n):
    arr=[[0]*n for _ in range(n)]
    
    dx=[0,1,0,-1] #행이동  행이 위아래로 이동하는 것이니까 dx
    dy=[1,0,-1,0] #열이동  열이 좌우로 이동하는 것dlslRk dy
    
    x,y, direction = 0,0,0 # 시작위치 방향 오른쪽
    # 순서가 오른족 아래 왼쪽 위 이렇게 0,1,2,3이 됨
    # 따라서 direction 0은 오른쪽 direction 1은 아래
    
    for num in range(1, n*n+1):
        arr[x][y] = num
        nx, ny = x+dx[direction], y+dy[direction]
        # 다음위치계산
        if not(0 <=nx<n and 0<=ny<n and arr[nx][ny]==0):
            direction = (direction +1)%4
            # 방향 변경(오른쪽->아래->왼쪽->위)
            nx, ny = x+dx[direction], y+dy[direction] # 방향을 바꾼 후 다시 이동
        x,y = nx,ny # 새로운 위치로 이동
        
    return arr
        
    
    
    