def solution(myString):
    return sorted(s for s in myString.split('x') if s) 

# 특정단어 split('x')을 기준으로 자르고 문자열만들어서 sorted()사전순서로 배열

#solution = lambda myString : sorted([s for s in myString.split('x') if s ])
# s는 진리값, 공백문자열' ' 은 falsy한 값으로 간주