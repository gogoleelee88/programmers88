def solution(picture, k):
    answer = []
    
    for row in picture:
        # 가로 방향으로 k배 확장
        expanded_row = ''.join([char * k for char in row])
        
        # 세로 방향으로 k배 추가
        for _ in range(k):
            answer.append(expanded_row)
    
    return answer


#for i in range(len(picture)):
#    for_ in range(k):
#        answer.append(picture[i].replace('.','.'*k).replace('x',"x"*k))
#    return answer