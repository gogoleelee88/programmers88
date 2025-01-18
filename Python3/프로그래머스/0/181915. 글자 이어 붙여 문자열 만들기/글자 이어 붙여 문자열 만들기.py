def solution(my_string, index_list):
    answer = ''
   


#index_list의 인덱스돌면서 값을 가져오고 그값에 대한 my_string에 문자를 가져오기

    for i in index_list:
        answer += my_string[i]  
    return answer

#answer = []  # 빈 리스트 생성
#answer.append(my_string[i])  # 리스트에 추가
#result = ''.join(answer)  # 리스트를 문자열로 합치기
#answer = ''  # 빈 문자열 생성
#answer += my_string[i]  # 문자열 이어붙이기

#def solution(my_string, index_list):
#    return ''.join(map(lambda x: my_string[x], index_list))

#def solution(my_string, index_list):
#    return ''.join([my_string[idx] for idx in index_list])




