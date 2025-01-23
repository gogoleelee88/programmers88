from functools import reduce
def solution(num_list):
    answer = 0
   

    for num in num_list:
        if len(num_list)>=11:
            answer+=num
        else:
            answer= reduce(lambda x,y:x*y, num_list)
    return answer

#from math import prod
#def solution(num_list):
#    return sum(num_list) if len(num_list)>=11 else prod(num_list)
# prod(리스트)는 리스트 안에 모든 값을 곱함 

#def solution(a):
#   if len(a)<=10:
#       total = 1
#       for i in a:
#       return total
#   else:
#       return sum(a)







