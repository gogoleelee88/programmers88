def solution(my_string, index_list):
    answer = ''
   


#index_list의 인덱스돌면서 값을 가져오고 그값에 대한 my_string에 문자를 가져오기

    for i in index_list:
        answer += my_string[i]  
    return answer