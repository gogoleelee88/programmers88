def solution(l, r):
    tmp = []

    # l부터 r까지 순회
    for x in range(l, r + 1):  # 범위 수정: l부터 r까지
        # '0'과 '5'만 포함하고, 5로 나누어떨어지는지 확인
        if all(digit in '05' for digit in str(x)) and x % 5 == 0:
            tmp.append(x)

    # 유효한 값이 없으면 [-1]을 리턴
    if not tmp:
        return [-1]

    # 결과는 오름차순으로 정렬
    tmp.sort()
    
    return tmp
