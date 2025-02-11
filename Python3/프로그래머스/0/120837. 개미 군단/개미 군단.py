def solution(hp):
    count=0
    gen=5
    sol=3
    work=1
# 우선 장군개미는 5, 병정개미는 3, 일개미1 이면 장군개미로 나누어목과 나머지를 구하고, 나머지를 병정개미
    while hp>=5:
        hp-=gen
        count+=1
    while hp>=3:
         hp-=sol
         count+=1
    return count+hp
