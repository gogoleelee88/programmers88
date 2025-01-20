def solution(arr, query):


   
    # 짝수인덱스면 query[i]이후 인덱스 버림
    # 홀수인덱스면 query[i]이전 인덱스 버림
    for i in range(len(query)):
        if i%2==0:
            arr = arr[:query[i]+1]    
        else:
            arr = arr[query[i]:]
    return arr


#def so3lution(arr, query):
#    for k, q in enumerate(query):
#        if k % 2 == 0:
#            arr = arr[:q + 1]
#        else:
#            arr = arr[q:]
#    return arr