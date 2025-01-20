def solution(arr):
    tmp=[]
# 2가 있는 인덱스를 찾고, 그인덱스범위를 리스트로 내보내기
    for i in range(len(arr)):
        if arr[i]==2:
            tmp.append(i)
    if not tmp:
        return [-1]
    return arr[min(tmp):max(tmp)+1]            


# def solution(arr):
    # 2가 배열에 없으면 [-1]을 반환
#    if 2 not in arr:
#        return [-1]
#    return arr[arr.index(2) : len(arr) - arr[::-1].index(2)]
    # arr.index(2):첫 번째 2의 위치
    #arr[::-1].index(2) 뒤집은 배열에서 첫번째 2의 위치
    #len(arr)-arr[::-1].index(2):원래 배열에서 마지막 2의 위치+1