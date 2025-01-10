def solution(ineq, eq, n, m):

# ineq와 eq를 정함. 
  
# 완성된조건식이 맞으면 1 아니면 0

    if eq=="!":
        eq=""
    return int(eval(str(n) + ineq + eq + str(m)))

#def solution(ineq, eq, n, m):
#    return int(eval(str(n)+ineq+eq.replace('!', '')+str(m)))
#replace!!!!!!!!!