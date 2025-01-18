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
# from collections import Counter
# def solution(a, b, c, d):
#     # Counter를 사용해 입력된 숫자들의 빈도 계산
#     counter = Counter([a,b,c,d])
#     # most_common()으로 빈도수가 높은 순으로 정렬된 리스트 생성
#     tmp = counter.most_common()
   
#     # 서로 다른 숫자의 개수에 따라 다른 계산 실행
#     match len(tmp):
#         # 모든 숫자가 같을 때 (예: 4444면 1111*4 = 4444 반환)
#         case 1:  
#             return 1111 * tmp[0][0]
           
#         # 두 종류의 숫자일 때 (예: 3332면 3이 3번, 2가 1번)    
#         case 2:  
#             # 2:2로 나뉜 경우 (예: 2244면 (2+4)*|2-4| = 6*2 = 12)
#             if tmp[0][1] == 2:  
#                 return (tmp[0][0] + tmp[1][0]) * abs(tmp[0][0] - tmp[1][0])
#             # 3:1로 나뉜 경우 (예: 3332면 (10*3+2)^2 = 32^2 = 1024)
#             return (10 * tmp[0][0] + tmp[1][0]) ** 2  
           
#         # 세 종류의 숫자일 때 (예: 2233이면 두 번째로 많은 숫자 * 가장 적은 숫자)    
#         case 3:  
#             return tmp[1][0] * tmp[2][0]
           
#         # 네 숫자가 모두 다를 때 (예: 1234면 min(1,2,3,4) = 1)    
#         case 4:  
#             return min(num for num, _ in tmp)        
            