def solution(my_string, n):
  
    return my_string[-n:]


# [:-n] 은 뒤에서 n개 제외한 나머지 가져옴
# [-n:]뒤에서부터 n개 가져옴
# [:n]처음부터 n-1개 가져옴
# [n:] n번부터 끝까지 가져옴

#def solution(my_string, n):
#    length=len(my_string)-n
#    answer = my_string[length:]
#    return answer