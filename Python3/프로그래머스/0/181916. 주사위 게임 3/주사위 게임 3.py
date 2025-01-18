from collections import Counter
def solution(a, b, c, d):
    answer = 0
    tmp=0
    counter = Counter([a,b,c,d])
    tmp = counter.most_common()
    print(tmp)
    

    if len(tmp) ==1:
        answer = 1111*tmp[0][0]
    elif len(tmp) ==2 and tmp[0][1]!=2:
        answer = (10*tmp[0][0]+tmp[1][0])**2
            
    elif len(tmp) ==2 and tmp[0][1]==2:
        answer = (tmp[0][0]+tmp[1][0])*abs(tmp[0][0]-tmp[1][0])
    elif len(tmp) ==3 and tmp[0][0]!=tmp[1][0]!=tmp[2][0]:
        answer = tmp[1][0]*tmp[2][0]    
    elif len(tmp) ==4:
        answer = min(tmp[0][0],tmp[1][0],tmp[2][0],tmp[3][0])
    return answer
        
            