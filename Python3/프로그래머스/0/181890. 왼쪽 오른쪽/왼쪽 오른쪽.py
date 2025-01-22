def solution(str_list):
    answer = []
    
    
    if   ('l' in str_list and  'r' not in str_list)or ('l' in str_list and 'r' in str_list and str_list.index('l')<str_list.index('r')):
        answer = str_list[:str_list.index('l')]
    elif ('r'in str_list and  'l' not in str_list)or('r' in str_list and 'l' in str_list and str_list.index('r')<str_list.index('l')):
        answer = str_list[str_list.index('r')+1:]
    return answer   
#l만있고, r이 없는 경우  이조건이 True면 뒤의 조건은 확인하지 않음 그래서 단락평가덕에 에러방지가능


#def solution(str_list):
#  for i in range(len(str_list)):
#      if str_list[i]=='l':return str_list[:i]
# l을 만나면 l이전의 리스트반환
#       elif str_list[i]=='r':retun str_list[i+1:]
#r을 만나면 r이전의 리스트 반환
#    return []


#def solution(str_list): 리스트의 인덱스와 값을 동시에 가져옴
#def solution(str_list):
#   for i,s in str_list:
#       if s=='i':
#            return str_list[:i]
#       elif s== 'r':
#            return str_list[i+1:]
#   return []
# range(len(str_list))를 사용하는 것보다 더 파이썬스러운 방법?