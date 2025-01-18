def solution(number):
    answer = 0


# 음이아닌 정수%9는 음이아닌 숫자의 각자리의 숫자의 합을 9로 나눈 나머지와 같다. 


    answer=sum(map(int,str(number)))%9
    return answer


#def solution(number):
#    return int(number) % 9

