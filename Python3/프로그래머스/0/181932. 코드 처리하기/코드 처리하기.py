def solution(code):
    answer = ''
    mode = 0  # 0: 일반 모드, 1: 1을 만난 후의 모드
    for idx in range(len(code)):
        if mode == 0:
            if code[idx] != '1':
                if idx % 2 == 0:  # 짝수 인덱스에서만
                    answer += code[idx]
            else:
                mode = 1  # 1을 만나면 mode를 1로 변경
        elif mode == 1:
            if code[idx] != '1':
                if idx % 2 == 1:  # 홀수 인덱스에서만
                    answer += code[idx]
            else:
                mode = 0  # 1을 만나면 mode를 다시 0으로 변경
    return answer if answer else "EMPTY"
