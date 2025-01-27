def solution(arr, k):
    result = []
    seen = set()
    
    # 중복을 제거하면서 앞에서부터 최대 k개의 수를 선택
    for num in arr:
        if num not in seen:
            seen.add(num)
            result.append(num)
        if len(result) == k:  # k개를 모두 채웠으면 중단
            break
    
    # 결과 배열의 길이가 k보다 작으면 -1로 채움
    while len(result) < k:
        result.append(-1)
    
    return result
