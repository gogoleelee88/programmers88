def solution(todo_list, finished):
    answer = []
   

# 두리스트를 묶어서 마치지 못한 일에 해당하는 값만 리스트로

    for a,b in zip(todo_list, finished):
        if not b: #if b=='false'는 안됨
            answer.append(a)
    return answer