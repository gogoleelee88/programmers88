def solution(str_list, ex):
    answer = ''
    
# ex 에 문자열에 있으면 제외하고 조인
  #  return ''.join(filter(lambda s: ex not in s,str_list ))

    filtered_list=[s for s in str_list if ex not in s]
    return "".join(filtered_list)