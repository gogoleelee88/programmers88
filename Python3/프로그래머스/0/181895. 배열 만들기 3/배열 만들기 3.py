def solution(arr, intervals):
    answer = []

    
    for [a,b] in intervals:
    # interval 의 값[a,b]가 arr의 [a:b+1]이됨
        answer+= arr[a:b+1]
    return answer