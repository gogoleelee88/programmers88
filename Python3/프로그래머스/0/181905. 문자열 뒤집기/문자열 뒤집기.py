def solution(my_string, s, e):
    answer = ''
   

    
    answer = my_string.replace(my_string[s:e+1],my_string[s:e+1][::-1])
    return answer

#def solution(my_string, s, e):
#    substr = reversed(list(my_string[s:e+1]))
#    return my_string[:s] + ''.join(substr) + my_string[e+1:]