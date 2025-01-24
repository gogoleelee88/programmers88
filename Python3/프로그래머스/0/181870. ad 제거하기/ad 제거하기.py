def solution(strArr):
    answer = []
   
# strArr 의 문자열에 ad가 있으면 제외

#    for a in strArr:
#        if 'ad' in a:
#            strArr.remove(a)
#    return strArr
# 이렇게하면 인덱스 순서가 꼬인다고 함. 

    return [a for a in strArr if 'ad' not in a]