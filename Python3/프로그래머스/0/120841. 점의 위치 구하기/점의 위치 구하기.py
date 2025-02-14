def solution(dot):


# dot[0]과 dot[1]이렇게 있으면 둘다 양수면,1
# x가 양수고, y가 음수면 


    
    if dot[0]>0 and dot[1]>0:
        return 1
    if dot[0]<0 and dot[1]>0:
        return 2
    if dot[0]<0 and dot[1]<0:
        return 3
    if dot[0]>0  and dot[1]<0:
        return 4
    
    
    # def solution(dot):
    #   quad = [[3,2], [4,1]] # 2차원 리스트로 변경
    #   retrun quad[dot[0]>0][dot[1]>0]
    
    # def solution(dot):
    # x,y = dot
    #if x*y >0:
    #   retrun 1 if x> 0 else 3
    #else:
    #   return 4 if x>0 else 2
    
    
    