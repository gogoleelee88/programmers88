def solution(a, b):
    
    a=str(a)
    b=str(b)
    answer = ''
    #a의 0번째 인덱스와 b의 0번째인덱스비교
    if a+b >= b+a:
        answer = a+b
    else:
        answer = b+a
        
    
    #a[0]이 크면 앞에 
    #아니면 뒤에

    return int(answer)