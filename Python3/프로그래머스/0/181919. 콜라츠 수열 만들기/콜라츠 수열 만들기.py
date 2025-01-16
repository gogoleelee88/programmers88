def solution(n):
    answer = []
    
# 처음 n을 리스트에넣고, 
    answer.append(n)
# n이 짝수면 2로 나누어 넣고 홀수면 3*X+1을 해서넣고
    while n > 1:
        if n%2==0:
            n=n//2
            answer.append(n)
        else:
            n=3*n+1
            answer.append(n)
    return answer

#모범 답안이란 같음