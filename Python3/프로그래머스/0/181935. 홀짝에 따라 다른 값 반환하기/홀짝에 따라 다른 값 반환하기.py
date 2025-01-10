
def solution(n):
    
    answer = 0 
# n이 홀수인지 짝수인지 확인
    if n%2!=0:
# 홀수면 n이하의 모든 정수의 합 
       answer = ((n+1)/2)**2
#아니면 n이하의 모든 짝수의 제곱의 합
    else : 
        for i in range(0,n+1,2):
            answer += i**2
    return answer