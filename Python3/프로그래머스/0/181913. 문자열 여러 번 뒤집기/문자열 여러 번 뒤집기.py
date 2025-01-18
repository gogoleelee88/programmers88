def solution(my_string, queries):
    answer = ''
    my_list=list(my_string)

# queries가 도는 동안 

    for start, end in queries:
# 해당 범위뒤집기
        my_list[start:end+1]= my_list[start:end+1][::-1]
    return ''.join(my_list)