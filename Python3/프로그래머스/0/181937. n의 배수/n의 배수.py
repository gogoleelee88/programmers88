def solution(num, n):
    answer = 0
    
    # num이 n의 배수 인지 확인
    answer = (int(num%n==0))
    # 맞으면 1, 아니면 0리턴
    return answer
 