def solution(arr, queries):




    # s,e,k 는 querues의 하나의 원소다. 
    
    # s<=i<=e 인 모든 i에 대해서 i가 k의 배수이면 arr[i]에 +1을 한다. 
        for i in range(len(arr)):
            for [s,e,k] in queries:
                if s<=i<=e and i%k==0:
                    arr[i]+=1
   # 여기  s<=i<=e 이조건을 쓰지 않았음
    # arr을 리턴한다.
        return arr
    
    
    #def solution(arr, queries):
    #for s, e, k in queries:
    #    for i in range(s, e+1):
    #        if i%k == 0:
    #            arr[i] += 1
    #return arr//
    
    
    
    