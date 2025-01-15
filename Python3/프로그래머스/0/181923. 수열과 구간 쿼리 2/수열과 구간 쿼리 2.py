def solution(arr, queries):
    answer = []

# queries에 각 원소는 [s,e,k], s<=i<=e인 모든 i>k 중에서 가장 작은 것 min
    for [s,e,k] in queries:
        A=[arr[x] for x in range(len(arr)) if s<=x<=e and arr[x]>k]
        if A:
            answer.append(min(A))        
        else:
                answer.append(-1)
    return answer

#def solution(arr, queries):
#    answer = []  # 최종 결과를 저장할 리스트
#쿼리 처리 
# for s,e,k in quries:  queries에서 값가져오고
#   tmp = [] #조건을 만족하는 값을 임시로 저장할 리스트
#   for x in arr[s:e+1] # arr의 s부터 e까지의 범위를 슬라이싱
# if x > k: #k보다 큰 값만 
# tmp.append(x) # tmp리스트에 추가
#answer.append(-1 if not tmp else min(tmp))
# tmp가 비어있으면 -1 

