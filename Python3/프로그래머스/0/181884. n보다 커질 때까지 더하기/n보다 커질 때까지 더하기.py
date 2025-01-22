def solution(numbers, n):
    answer = 0
   

    # numbers를 더하다가  n보다 커지면 브레이크
    for num in numbers:
        if answer<=n:
            answer+=num
        
    return answer