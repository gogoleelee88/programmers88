def solution(my_string, k):
    answer = ''
    i=0
    while i<k:
        answer += my_string
        i+=1
    return answer

#def solution(my_string, k):
#    return my_string*k