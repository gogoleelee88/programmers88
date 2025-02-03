def solution(order):
    answer = 0
  

# 아무거나 아메리카노 4500 카페라떼=5000
# 리스트 문자열에 아메리카노라는 단어가 있으면, 4500, 카페라떼라는 단어가 있으면 +5000
    for menu in order:
        if "americano" in menu or "anything" in menu:
            answer+=4500
        elif "cafelatte" in menu:
            answer+=5000
    return answer


#   answer = 0
#    for want in order
#        if 'latte' in want:
#            answer +=500
#        answer +=4500
#    return answer

#   return sum([5000 if "cafelatte in i  else 4500 for i in order"])