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
        
    
    
    #def solution(n):
#    answer = [[None for j in range(n)] for i in range(n)]
 #   move = [[0, 1], [1, 0], [0, -1], [-1, 0]]
 #   x, y, m = 0, 0, 0
 #   for i in range(1, n**2 + 1):
 #       answer[y][x] = i
 #       if y + move[m][0] >= n or x + move[m][1] >= n or answer[y + move[m][0]][x + move[m][1]]:
  #          m = (m + 1) % len(move)
  #      y, x = y + move[m][0], x + move[m][1]
  #  return answer

#def solution(n):
#    return [[ 4*i*(n-i) + (1+x+y - 2*i if (x==i or y==n-i-1) else (4*n - 6*i - x - y -3))  for i,x,y in row]   for row in [[(min(n-x-1,x,n-y-1,y),x,y) for y in range(n)] for x in range(n)]]

